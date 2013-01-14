# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class IkeaItem(Item):
	
	name = Field()
	thing = Field()
	translation = Field()
	

