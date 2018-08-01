import json
from pprint import pprint



class json_item():
    with open('/home/solteee/community/items.json') as data_file:
        item = json.load(data_file)

    pprint(item)

