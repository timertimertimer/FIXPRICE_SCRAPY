import re
from time import time
from typing import Any
from scrapy import Spider
from scrapy.http import Response

from fixprice.config import CATEGORIES, LOCALITY
from fixprice.items import FixPriceItem


class FixPriceSpider(Spider):
    name = "fixprice"
    start_urls = CATEGORIES

    def parse(self, response: Response, **kwargs: Any) -> Any:
        items = response.css(".product__wrapper")
        for item in items:
            yield response.follow("https://fix-price.com" + item.css("a::attr(href)").get(), callback=self.parse_item)

        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow("https://fix-price.com" + next_page, callback=self.parse)

    def parse_item(self, response: Response, **kwargs: Any) -> Any:
        fp_item = FixPriceItem()
        fp_item["timestamp"] = int(time())
        fp_item["url"] = response.url

        titles = response.css(".property .title::text").getall()
        values = response.css(".property .value *::text").getall()
        properties = dict(zip(titles, values))
        fp_item["brand"] = properties.pop("Бренд", "")
        fp_item["rpc"] = properties.pop("Код товара", "")
        fp_item["metadata"] = {
            "__description": response.css("div[data-v-5e0bc2b1].description::text").get()
        } | properties

        fp_item["title"] = response.css("h1[data-v-5e0bc2b1]::text").get()
        fp_item["marketing_tags"] = [] # TODO
        fp_item["section"] = [el.css("span::text").get() for el in response.css("div.crumb")[2:-1]]

        if response.css(".out-of-stock"):
            fp_item["price_data"] = dict(current=0, original=0, sale_tag=0)
            fp_item["stock"] = {"in_stock": False, "count": 0}
        else:
            original_price = float(response.css('meta[itemprop="price"]::attr(content)').get())

            match = re.search(
                r"specialPrice:(\{.*?\})",
                response.xpath("//script[contains(text(), 'specialPrice')]/text()").extract_first(""),
            )
            if match:
                special_price = re.search(r'price:"([^"]+)"', match.group(1))
            special_price = float(special_price.group(1)) if special_price else original_price
            discount_percentage = (original_price - special_price) / original_price * 100
            fp_item["price_data"] = {
                "current": special_price,
                "original": original_price,
                "sale_tag": f"Скидка {discount_percentage:.2f}%",
            }

        images = response.css(".product-images .normal::attr(src)").getall()
        fp_item["assets"] = {
            "main_image": images[0],
            "set_images": images,
            "view360": [],  # TODO
            "video": [],  # TODO
        }
        fp_item["variants"] = 1 # TODO

        if "stock" not in fp_item:
            yield response.follow(
                f"https://api.fix-price.com/buyer/v1/store/balance/{fp_item['rpc']}?canPickup=all&addressPart=&inStock=true",
                callback=self.parse_stock_data,
                headers={"X-City": LOCALITY["cityId"]},
                meta={"fp_item": fp_item},
            )
        else:
            yield fp_item

    def parse_stock_data(self, response: Response, **kwargs: Any) -> Any:
        fp_item = response.meta["fp_item"]
        city_data = response.json()
        if not city_data:
            fp_item["stock"] = {"in_stock": False, "count": 0}
        else:
            count = 0
            for shop in city_data:
                count += shop["count"]
            fp_item["stock"] = {"in_stock": True, "count": count}
        yield fp_item
