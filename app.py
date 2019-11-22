import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'MS3_project'
app.config["MONGO_URI"] = 'mongodb+srv://rOOtUser:betteroption@myfirstcluster-97xkz.mongodb.net/MS3_project?retryWrites=true&w=majority'
#os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("firstSteps.html", firstSteps=mongo.db.firstSteps.find())

@app.route('/add_tasks')
def add_tasks():
    return render_template("myProblem.html", myProblem=mongo.db.myProblem.find())

@app.route('/insert_task', methods=['POST'])
def insert_task():
    myProblem = mongo.db.myProblem
    print(request.form)
    myProblem.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
  

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)


