#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from MongoDB import MongoDB
token = "EAAW32eEZApB0BAHyqPoG1RCLZACwlgi8xzcWFCxz34JTwHAkZCYy63Kywxp9weNSUUKtzxeGS3DLV76z1zg6vfHOwqM22bG3QcIIzWW42EN8iwbqGwgHX7ryDtvx6T3dP0YrUwqRHKpX9MrVfR5BCrTclDZC6Ip7akR0o0XXz2UZBqbZBjzmrTCOj9MhYiOZBcZD"
link_api = "https://graph.facebook.com/me?fields=posts&access_token="+token
resp = requests.get(link_api)
data = resp.json()
db = MongoDB("facebook")
# print(data["posts"]["data"])

#create db if db not exist

#collection
# postid_col = db.connect("postID")
postcontent_col = db.connect("posts")
#data get from facebook
datapost = list(data["posts"]["data"])
name = "tatnh"
for dp in datapost:
    if "message" in dp:
        content = dp["message"]
        created_time = dp["created_time"]
        id_post = dp["id"]
        postcontent_col.update({"_id":id_post},{"$set":{"content":content, "name":name, "_id":id_post, "created_time":created_time}}, upsert=True)
        # postcontent_col.remove()
db.disconnect()
