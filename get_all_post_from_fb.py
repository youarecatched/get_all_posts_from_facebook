#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from MongoDB import MongoDB
token = "EAAW32eEZApB0BACqDNm1LNbSja8neci6xqCYEXSyidzPMnTdETeIUWMSEbUD1hjWAeUoRUuNDe0SDcvzY0klezZAfyrJdolJqwy0KFkRGb7ucMTvXFEJPUj6xBjHMZBwajjm6BGuoySCtxld4fsC3yohkVYok3D8a8PE1iCIrGVtE35PVdYWS9uIb1YNXAZD"
link_api = "https://graph.facebook.com/me?fields=posts&access_token="+token
resp = requests.get(link_api)
data = resp.json()
db = MongoDB("facebook")
# print(data["posts"]["data"])

#create db if db not exist
with db.open("posts") as dbpost:
    name = "tatnh"
    # print(data)
    datapost = data["posts"]["data"]
    dbpost.update({"_id":name},{"$set":{"data":datapost, "_id":name}}, upsert=True)
    dbpost.remove()
    # data = dbpost.find_one({})
    # print(data)

