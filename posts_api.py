#!/usr/bin/python
# -*- coding: utf-8 -*-
import flask
import re
from flask import request, abort, jsonify
from MongoDB import MongoDB
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route("/posts/search", methods=["POST"])
def get_posts():
    db = MongoDB("facebook")
    search_term = request.args.get('q')
    data = None
    with db.open("posts") as dbpost:
        find_ = re.compile(search_term, re.IGNORECASE)
        data = list(dbpost.find({"name":"tatnh", "content":{"$regex":find_}}))
    if not data:
        return "NULL"
    list_content = []
    for ct in data:
        if "content" in ct:
            content = ct["content"]
            if search_term.lower() in content.lower():
                content = content
                list_content.append({"content": content.encode("utf-8").decode("utf-8")})
    return jsonify({"data":list_content})
app.run(host='localhost', port=3000)
