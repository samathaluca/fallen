import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
# from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["MONGO_DBNAME"] = 'MS3_project'

mongo = PyMongo(app)

def index():
    changes=mongo.db.changes.find()
    return changes

def test_index():
    assert index() != None
mongo = PyMongo(app)

if __name__ == "__main__":
    test_index()
    print("Everything passed")






# for doc in documents:
#     print(doc)
@app.route('/')
def hello():
    return "ALL GOOD"


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)
