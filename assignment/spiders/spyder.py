from unicodedata import name
import scrapy

class Spider(scrapy.Spider):
    name = 'items'
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1',
    'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=2']

    def parse(self, response):
        for product in  response.css('div.product'):
            yield {
                'title':product.css('a.catalog-item-name::text').get(),
                'price':product.xpath('div[2]/div/span/span/text()').get(),
                'stock': False if product.css('span.out-of-stock::text').get()=='Out of Stock' else True,
                'manufacturer':product.css('a.catalog-item-brand::text').get(),
                'review':product.css('span.pr-accessible-text::text').get()
            }
