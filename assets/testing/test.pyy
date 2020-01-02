import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
# from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["MONGO_DBNAME"] = 'MS3_project'

mongo = PyMongo(app)

# Early tests
@app.route('/')
def hello():
    return "ALL GOOD"

#October/November tests
'''
When struggling coding the Update CRUD function, I broke the problem down as follows to test if Flask could return anything in isolation.
I substituted the results of the Mongo query with a python class containing test data, to see if the problem with flask or mongo. 
If flask could return the test data then the problem must be with mongoDB not the python code.
The result of this test was that flask returned test data fine so I knew the problem was with mongo and 
I later noticed a spelling mistake in the names of the field/ attribute within  mongo documents.

'''



{% extends 'base.html' %}
  <h1>alias id: {{ alias.id }}!</h1>
    <h1>Helloapp {{ alias.username }}!</h1>
    <h1>password: {{ alias.password }}!</h1>
    <form action="{{ url_for('alias')}}" method="POST"  class="col s12">
  {% endfor %}


class aliasx:
    username = 'hhh'
    password = 'uuu'

@app.route('/alias')
def alias():
    # return render_template('alias.html', alias=mongo.db.user.find())
    return render_template('alias.html', alias=mongo.db.user.find_one())
    # return render_template('alias.html', alias=aliasx())




Ran test then found request.form.get('firat') should be request.form.get('first')

# @app.route('/update_editSteps/<editSteps_id>', methods=['GET', 'POST'])
# def update_editSteps(editSteps_id):
#     editSteps = mongo.db.editSteps
#     editSteps.update({'editSteps_id': ObjectId(editSteps_id)},
#                      {'first': request.form.get('firat'),
#                       'second': request.form.get('second'),
#                       'third': request.form.get('third'),
#                       'fourth': request.form.get('fourth'),
#                       'fifth': request.form.get('fifth')})
#     return redirect(url_for('index'))


def index():
    changes=mongo.db.changes.find()
    return changes

def test_index():
    assert index() != None
mongo = PyMongo(app)

if __name__ == "__main__":
    test_index()
    print("Everything passed")


    if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)


https://docs.pytest.org/en/latest/getting-started.html

pip install -U pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
  




@app.route('/imageTest')
def imageTest():
    return render_template('imageTest.html')
