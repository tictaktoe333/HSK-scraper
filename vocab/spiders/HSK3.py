import scrapy


class Hsk3Spider(scrapy.Spider):
    name = "HSK3"
    allowed_domains = ["hsk.academy"]
    start_urls = ["http://hsk.academy/en/hsk-3-vocabulary-list"]

    def parse(self, response):
        words = response.xpath(
            "/html/body/section/div/div[1]/div[2]/div/div[3]/div[2]/div/table/tbody/tr")
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        with open("HSK3.md", "w") as f:
            f.write("|      English     | Mandarin | Pinyin |\n")
            f.write("| ---------------- | -------- | ------ |\n")
            for word in words:
                english = word.css("td:nth-child(2)::text").get()
                mandarin = word.css("td:nth-child(1) > a::text").get()
                pinyin = \
                    word.css("td:nth-child(1) > a::text").getall()[1].strip()
                f.write(f"| {english} | {mandarin} | {pinyin} |\n")
            f.close()
