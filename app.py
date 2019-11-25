import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'MS3_project'
app.config["MONGO_URI"] = 'mongodb+srv://rOOtUser:betteroption@myfirstcluster-97xkz.mongodb.net/MS3_project?retryWrites=true&w=majority'
# os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/firstSteps')
def firstSteps():
    return render_template('firstSteps.html', firstSteps=mongo.db.firstSteps.find())

@app.route('/myProblem')
def myProblem():
    return render_template('myProblem.html', myProblem=mongo.db.myProblem.find())

@app.route('/insert_form', methods=['POST'])
def insert_form():
    myProblem =  mongo.db.myProblem
    myProblem.insert_one(request.form.to_dict())
    return redirect(url_for('myProblem'))

# @app.route('/edit_task/<task_id>')
# def edit_task(task_id):
#     the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
#     all_categories =  mongo.db.categories.find()
#     return render_template('edittask.html', task=the_task,
#                            categories=all_categories)


# @app.route('/update_task/<task_id>', methods=["POST"])
# def update_task(task_id):
#     tasks = mongo.db.tasks
#     tasks.update( {'_id': ObjectId(task_id)},
#     {
#         'task_name':request.form.get('task_name'),
#         'category_name':request.form.get('category_name'),
#         'task_description': request.form.get('task_description'),
#         'due_date': request.form.get('due_date'),
#         'is_urgent':request.form.get('is_urgent')
#     })
#     return redirect(url_for('get_tasks'))


# @app.route('/delete_task/<task_id>')
# def delete_task(task_id):
#     mongo.db.tasks.remove({'_id': ObjectId(task_id)})
#     return redirect(url_for('get_tasks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)


