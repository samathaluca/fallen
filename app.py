import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'MS3_project'
# MONGO_URI = os.environ.get('MONGO_URI')
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

# app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
# app.config["MONGO_DBNAME"] = 'MS3_project'
# app.config["MONGO_DBNAME"] = 'changes'


mongo = PyMongo(app)

# MONGO_URI = os.environ.get('MONGO_URI')
# MONGODB_URI = os.getenv("MONGO_URI")


@app.route('/')
@app.route('/index')
def index():

    changes=mongo.db.changes.find()
    return render_template('index.html', categories=mongo.db.categories.find(), changes=mongo.db.changes.find())



# 


@app.route('/changes', methods=['GET', 'POST'])
def changes():
    
    if request.method == 'GET':
        return render_template('changes.html', changes=mongo.db.changes.find())
       
    else:
        
        habit=(request.form.get("habit"))
        print(habit)
        #  Cool! We found the value!  Now lets search
        changes = mongo.db.changes.find({"habit":habit})
        # Did we get results?  Lets check by rendering them
        return render_template('changes.html', changes=changes)

# @app.route('/deleteButton', methods=['GET', 'POST'])
# def deleteButton():
#     # gets all Changes if method is a GET
#     if request.method == 'GET':
#         return render_template('deleteButton.html', changes=mongo.db.changes.find())
#         # if we have a POST, lets use the form we posted
#     else:
#         #Let check if we are able to get the habit - habit is the name of the field
#         habit=(request.form.get("habit"))
#         print(habit)
#         #  Cool! We found the value!  Now lets search
#         changes = mongo.db.changes.find({"habit":habit})
#         # Did we get results?  Lets check by rendering them
#         return render_template('deleteButton.html', changes=changes)




# In the GET
# myProblem just changes to changes.  Its the exact same bit of logic. 

@app.route('/deleteButton')
def deleteButton():
    return render_template('deleteButton.html', changes=mongo.db.changes.find())

@app.route('/add_changes')
def add_changes():
    return render_template('add_changes.html', categories=mongo.db.categories.find())


@app.route('/insert_changes', methods=['POST'])
def insert_changes():
    changes = mongo.db.changes
    changes.insert_one(request.form.to_dict())
    return redirect(url_for('changes'))

@app.route('/edit_changes/<changes_id>')
def edit_changes(changes_id):
    the_change = mongo.db.changes.find_one({"_id": ObjectId(changes_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_changes.html', changes=the_change, categories=all_categories)

@app.route('/update_changes/<changes_id>', methods=["POST"])
def update_changes(changes_id):
    changes = mongo.db.changes
    changes.update({'_id': ObjectId(changes_id)},
    {
        'alias':request.form.get('alias'),
        'habit':request.form.get('habit'),
        'start_date':request.form.get('start_date'),
        'whyStop':request.form.get('whyStop'),
        'whatStop':request.form.get('whatStop'),
        'feelings':request.form.get('feelings'),
        'recipe':request.form.get('recipe'),
        'ingredients':request.form.get('ingredients'),
        'day1':request.form.get('day1'),
        'day2':request.form.get('day2'),
        'day3':request.form.get('day3'),
        'week1':request.form.get('week1'),
        'week2':request.form.get('week2'),
        'week3':request.form.get('week3'),
        'year1':request.form.get('year1'),
        'year2':request.form.get('year2'),
        'year3':request.form.get('year3'),
    })
    return redirect(url_for('changes'))

@app.route('/delete_changes/<changes_id>')
def delete_changes(changes_id):
    mongo.db.changes.remove({'_id': ObjectId(changes_id)})
    return redirect(url_for('changes'))



@app.route('/storyDetail/<changes_id>', methods=['GET', 'POST'])
def storyDetail(changes_id):
    # print(changes_id)
#   """
#   Given story ID get a specific user story.
#   """
# Render HTML page for 1 document, pulled from the database.
    changes = mongo.db.changes.find_one({'_id': ObjectId(changes_id)})
    return render_template('storyDetail.html', changes=changes)
                #   <any other variables you want to pass on to template>)

# def create_story():
  # Do whatever you're doing so far to insert a story
  # Saving a story to database should return an object with the story id in an attribute
  # called inserted_id. See https://www.w3schools.com/python/python_mongodb_insert.asp

    # new_story = mongo.db.changes.insert_one(changes)
    # story_id = new_story.inserted_id
    # return redirect(url_for('storyDetail', changes_id=changes_id))

@app.route('/firstSteps')
def firstSteps():
    return render_template('firstSteps.html', firstSteps=mongo.db.firstSteps.find())

@app.route('/imageTest')
def imageTest():
    return render_template('imageTest.html')

@app.route('/myProblem', methods=['GET', 'POST'])
def myProblem():
    if request.method == 'GET':
        return render_template('myProblem.html', myProblem=mongo.db.myProblem.find())
    else:
        insert_myProblem = mongo.db.myProblem
        insert_myProblem.insert_one(request.form.to_dict())
        return redirect(url_for('index'))

@app.route('/pastProblem', methods=['GET', 'POST'])
def pastProblem():
    if request.method == 'GET':
        return render_template('pastProblem.html', pastProblem=mongo.db.pastProblem.find())
    else:
        insert_pastProblem = mongo.db.pastProblem
        insert_pastProblem.insert_one(request.form.to_dict())
        return redirect(url_for('index'))


@app.route('/tasks')
def tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


@app.route('/nineMinutes', methods=['GET', 'POST'])
def nineMinutes():
    if request.method == 'GET':
        return render_template('nineMinutes.html', nine_minutes=mongo.db.nineMinutes.find())
    else:
        insert_nineMinutes = mongo.db.nineMinutes
        insert_nineMinutes.insert_one(request.form.to_dict())
        return redirect(url_for('index'))


# @app.route('/nineMinutesUpdate', methods=['GET', 'POST'])
# def nineMinutesUpdate():
#     if request.method == 'GET':
#         return render_template('nineMinutes.html', nine_minutes=mongo.db.nineMinutes.find())
#     else:
#         insert_nineMinutes = mongo.db.nineMinutes
#         insert_nineMinutes.insert_one(request.form.to_dict())
#         return redirect(url_for('index'))


@app.route('/nineMinutesUpdate', methods=['GET', 'POST'])
def nineMinutesUpdate():
    if request.method == 'GET':
        return render_template('nineMinutesUpdate.html', nine_minutes=mongo.db.nineMinutes.find())
    else:
        insert_nineMinutes = mongo.db.nineMinutes
        insert_nineMinutes.insert_one(request.form.to_dict())
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)
