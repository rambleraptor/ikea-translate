import json

json_file = open('scraped_data_utf8.json')
data = json.load(json_file)
json_file.close()

# print data