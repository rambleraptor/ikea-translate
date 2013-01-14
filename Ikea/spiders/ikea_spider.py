from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import urllib, urllib2
import json
from lxml import etree
# //span[contains(@class, "productsAzLink")]/a/text()
from Ikea.items import IkeaItem
class IkeaSpider(BaseSpider):
	name = "ikea"
	allowed_domains = ["www.ikea.com/us/en/catalog/productsaz/"]
	base_url = "http://www.ikea.com/us/en/catalog/productsaz/"
	start_urls = []
	for i in range(26):
		url = base_url + str(i)
		start_urls.append(url)
		
		
	
	def parse(self,response):
		#Get Access Token for Microsoft Translate
	
		
		atrequest = urllib2.Request('https://datamarket.accesscontrol.windows.net/v2/OAuth2-13')
		atrequest.add_data(atdata)
		atresponse = urllib2.urlopen(atrequest)
		access_token = json.loads(atresponse.read())['access_token']
		
		hxs = HtmlXPathSelector(response) 
		sites = hxs.select('//span[contains(@class, "productsAzLink")]/a/text()').extract()
		items = []
		
		for site in sites:
			text = []
			item = IkeaItem()
			item['name'],_,item['thing'] = unicode(site).partition(' ')
			
			tosend = {'text': unicode(item['name']), 'from' : 'sv' , 'to' : 'en' }
			request = urllib2.Request('http://api.microsofttranslator.com/v2/Http.svc/Translate?'+urllib.urlencode(tosend))
			request.add_header('Authorization', 'Bearer '+access_token)
			response = urllib2.urlopen(request)
			doc = etree.fromstring(response.read())
			
			for elem in doc.xpath('/foo:string', namespaces={'foo': 'http://schemas.microsoft.com/2003/10/Serialization/'}):
				if elem.text:
					elem_text = ' '.join(elem.text.split())
					if len(elem_text) > 0:
						text.append(elem_text)
		
			item['translation'] = ' '.join(text)
			items.append(item)
		return items