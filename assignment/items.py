# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import scrapy


class AssignmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price=scrapy.Field()
    title=scrapy.Field()
    stock=scrapy.Field()
    manufacturer=scrapy.Field()
    review=scrapy.Field()
    
