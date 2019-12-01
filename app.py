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

@app.route('/myProblem', methods=['GET', 'POST'])
def myProblem():
    if request.method == 'GET':
        return render_template('myProblem.html', myProblem=mongo.db.myProblem.find())
    else:
        insert_myProblem = mongo.db.myProblem
        insert_myProblem.insert_one(request.form.to_dict())
        return redirect(url_for('index'))


# class aliasx:
#     username = 'hhh'
#     password = 'uuu'

@app.route('/alias')
def alias():
    # return render_template('alias.html', alias=mongo.db.user.find())
    return render_template('alias.html', alias=mongo.db.user.find())
    # return render_template('alias.html', alias=aliasx())

# @app.route('/users/')
# def users():
#     users = User.objects.all()
#     return render_template('users.html', u=users)
    
# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('hello.html', name = user)

@app.route('/alias/<alias_id>', methods=['POST'])
def editAlias(alias_id):
    editAlias = { '_id': (alias_id) }
    newvalues = { "$set": { "username": request.form.get('username'), "password": request.form.get('password') } }
    mongo.db.user.update(editAlias, newvalues)
    return redirect(url_for('aliasConfirmed'))





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

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')), 
            debug=True)


# @app.route('/editSteps', methods=['GET', 'POST'])
# def editSteps():
#     if request.method == 'GET':
#         return render_template('editSteps.html', editSteps=mongo.db.editSteps.find())
#     else:
#         insert_editSteps = mongo.db.editSteps
#         insert_editSteps.insert_one(request.form.to_dict())


#         return redirect(url_for('index'))


# @app.route('/edit_task/<task_id>')
# def edit_task(task_id):
#     the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
#     all_categories =  mongo.db.categories.find()
#     return render_template('task.html', task=the_task,
#                            categories=all_categories)

# @app.route('/edit_category/<category_id>')
# def edit_category(category_id):
#     return render_template('editcategory.html',
#     category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))

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

# @app.route('/update_category/<category_id>', methods=['POST'])
# def update_category(category_id):
#     mongo.db.categories.update(
#         {'_id': ObjectId(category_id)},
#         {'category_name': request.form.get('category_name')})
#     return redirect(url_for('get_categories'))



# @app.route('/delete_task/<task_id>')
# def delete_task(task_id):
#     mongo.db.tasks.remove({'_id': ObjectId(task_id)})
#     return redirect(url_for('get_tasks'))





# @app.route('/delete_category/<category_id>')
# def delete_category(category_id):
#     mongo.db.categories.remove({'_id': ObjectId(category_id)})
#     return redirect(url_for('get_categories'))

# @app.route('/update_task/<editSteps_id>', methods=["POST"])
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