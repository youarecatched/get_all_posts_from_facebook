import flask
from flask import request, abort, jsonify
from MongoDB import MongoDB
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/posts/search", methods=["POST"])
def get_posts():
    db = MongoDB("facebook", "tatnh", "123456")
    search_term = request.args.get('q')
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
            if search_term in content:
                list_content.append({"content":content})
    return jsonify({"data":list_content})

app.run(host='localhost', port=3000)
