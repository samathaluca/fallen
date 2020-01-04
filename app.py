import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists('env.py'):
    import env


# Create instance of Flask and assign it to 'app'
app = Flask(__name__)

# MongoDB assign db/ URI
app.config['MONGO_DBNAME'] = 'MS3_project'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

# Home page (index.html)
@app.route('/')
# @app.route('/index')
def index():
    '''
    pulls changes and categories collections from the MS3-project mongoDB to
    render in index.html.
    '''
    changes = mongo.db.changes.find()
    return render_template('index.html', categories=mongo.db.categories.find(), changes=mongo.db.changes.find())


# Tell your story page = myProblem.html
@app.route('/myProblem', methods=['GET', 'POST'])
def myProblem():
    '''
    Creates documents in the myProblem collection in the MS3-project mongoDB.
    Each document represents one completed 'Tell your story' created by this
    function.
    '''
    if request.method == 'GET':
        return render_template('myProblem.html', myProblem=mongo.db.myProblem.find())
    else:
        insert_myProblem = mongo.db.myProblem
        insert_myProblem.insert_one(request.form.to_dict())
        # return redirect(url_for('index'))
        return render_template('about_us.html')

# Recovery stories page = changes.html
@app.route('/changes', methods=['GET', 'POST'])
def changes():
    '''
    Reads changes collection in the MS3-project mongoDB to
    render in changes.html.
    All documents from changes collection are rendered as a list.
    '''
    if request.method == 'GET':
        return render_template('changes.html', changes=mongo.db.changes.find())
    else:
        habit = (request.form.get('habit'))
        changes = mongo.db.changes.find({'habit': habit})
        return render_template('changes.html', changes=changes)


# add recovery stories to mongoDB changes collection page (add_changes.html)
@app.route('/add_changes')
def add_changes():
    '''
    Pulls categories collection in to add_changes.html form.
    Renders add_changes_html page.
    '''
    return render_template('add_changes.html', categories=mongo.db.categories.find())


@app.route('/insert_changes', methods=['POST'])
def insert_changes():
    '''
    Creates documents in the changes collection in the MS3-project mongoDB.
    Each document represents one completed 'Share your recovery' created by
    this function.
    '''
    # changes = mongo.db.changes
    mongo.db.changes.insert_one(request.form.to_dict())
    return redirect(url_for('changes'))


# Edit recovery stories in mongoDB changes collection page (edit_changes.html)
@app.route('/edit_changes/<changes_id>', methods=['GET', 'POST'])
def edit_changes(changes_id):
    '''
    Pulls categories and changes collections in to edit_changes.html form.
    Renders edit_changes_html page.
    '''
    the_change = mongo.db.changes.find_one({'_id': ObjectId(changes_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_changes.html', changes=the_change, categories=all_categories)


@app.route('/update_changes/<changes_id>', methods=['POST'])
def update_changes(changes_id):
    '''
    Updates documents in the changes collection in the MS3-project mongoDB.
    '''
    changes = mongo.db.changes
    changes.update({'_id': ObjectId(changes_id)}, {
        'alias': request.form.get('alias'),
        'habit': request.form.get('habit'),
        'start_date': request.form.get('start_date'),
        'whyStop': request.form.get('whyStop'),
        'whoStop': request.form.get('whoStop'),
        'feelings': request.form.get('feelings'),
        'rockBottom': request.form.get('rockBottom'),
        'recipe': request.form.get('recipe'),
        'ingredients': request.form.get('ingredients'),
        'dayToDay': request.form.get('dayToDay'),
        'day1': request.form.get('day1'),
        'day2': request.form.get('day2'),
        'day3': request.form.get('day3'),
        'week1': request.form.get('week1'),
        'week2': request.form.get('week2'),
        'week3': request.form.get('week3'),
        'month1': request.form.get('month1'),
        'month2': request.form.get('month2'),
        'month3': request.form.get('month3'),
        'year1': request.form.get('year1'),
        'year2': request.form.get('year2'),
        'summary': request.form.get('summary'),
    })
    return redirect(url_for('changes'))


# Edit/Delete recovery stories, from mongoDB changes collection.
@app.route('/deleteButton')
def deleteButton():
    '''
    Renders deleteButton.html page with list of all change documents fro
    mongoDB.
    '''
    return render_template('deleteButton.html', changes=mongo.db.changes.find())


# delete recovery stories from mongoDB changes collection
@app.route('/delete_changes/<changes_id>')
def delete_changes(changes_id):
    '''
    Deletes selected document from changes collection in mongoDB.
    '''
    mongo.db.changes.remove({'_id': ObjectId(changes_id)})
    return redirect(url_for('changes'))


# individual recovery story page loaded from View story links
@app.route('/storyDetail/<changes_id>', methods=['GET', 'POST'])
def storyDetail(changes_id):
    '''
    A single document from changes collection,selected by id, is rendered as a
    single storyDetail.html page.
    '''
    changes = mongo.db.changes.find_one({'_id': ObjectId(changes_id)})
    return render_template('storyDetail.html', changes=changes)


# soul searching form page (pastProblem.html)
@app.route('/pastProblem', methods=['GET', 'POST'])
def pastProblem():
    '''
    Reads pastProblem collection in the MS3-project mongoDB to
    render in pastProblem.html.
    Creates documents in the pastProblem collection in the MS3-project mongoDB.
    Each document represents one completed 'Sould searching' form completion
    created by this function.
    '''
    if request.method == 'GET':
        return render_template(
            'pastProblem.html', pastProblem=mongo.db.pastProblem.find())
    else:
        insert_pastProblem = mongo.db.pastProblem
        insert_pastProblem.insert_one(request.form.to_dict())
        return redirect(url_for('index'))


@app.route('/gratitudeList')
def gratitudeList():
    '''
    Renders gratitudeList.html page.
    '''
    return render_template('gratitudeList.html')


@app.route('/about_us')
def about_us():
    '''
    Renders about_us.html page.
    '''
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=False)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0',
#             port=int(os.environ.get('PORT')),
#             debug=True)
