base_url = "http://www.ikea.com/us/en/catalog/productsaz/"
url_list = []
for i in range(26):
	url = base_url + str(i)
	url_list.append(url)
	
print url_list