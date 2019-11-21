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
@app.route('/get_persona')
def get_tasks():
    return render_template("persona.html",
                           persona=mongo.db.persona.find())


# @app.route('/add_task')
# def add_task():
#     return render_template('addtask.html',
#                            categories=mongo.db.categories.find())


# @app.route('/insert_task', methods=['POST'])
# def insert_task():
#     tasks = mongo.db.tasks
#     tasks.insert_one(request.form.to_dict())
#     return redirect(url_for('get_tasks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
