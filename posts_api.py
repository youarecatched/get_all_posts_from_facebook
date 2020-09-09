import flask
from flask import request, abort, jsonify
from MongoDB import MongoDB
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/posts/search=<pattern>", methods=["POST"])
def get_posts(pattern):
    db = MongoDB("facebook", "tatnh", "123456")
    print("str:",repr(pattern))
    with db.open("post") as dbpost:
        data = dbpost.find_one({"_id":"tatnh"})
    if not data:
        return "NULL"
    else:
        data = data["data"]
    list_content = []
    for ct in data:
        if "message" in ct:
            content = ct["message"]
            if pattern in content:
                list_content.append({"content":content})
    return jsonify({"data":list_content})

app.run(host='localhost', port=3000)
