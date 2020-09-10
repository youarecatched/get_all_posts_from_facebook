import requests
from MongoDB import MongoDB
token = "EAAW32eEZApB0BAF0etPtHZB9QMKrduFdOfBIgfLEcTUSIjZBX5PGZCpLl3YX4rpWLA7b980NaxlDWWSmQZBbZAg9w3UKBG7JT6VUGbpzOr5ERkcZCkt9stIliLYuepBu8lWxqC8uNPrZBScD74PppY7NSKr1ZCZAEhiEgmwZAyjrNlUTn7YMnkeYa6YwfwoSsZCeDVAZD"
link_api = "https://graph.facebook.com/me?fields=posts&access_token="+token
resp = requests.get(link_api)
data = resp.json()
db = MongoDB("facebook", "tatnh", "123456")
# print(data["posts"]["data"])
with db.open("post") as dbpost:
    name = "tatnh"
    datapost = data["posts"]["data"]
    dbpost.update({"_id":name},{"$set":{"data":datapost, "_id":name}}, upsert=True)
    # dbpost.remove()
    # data = dbpost.find_one({})
    # print(data)

