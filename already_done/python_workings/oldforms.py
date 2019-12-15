

# @app.route('/tasks')
# def tasks():
#     return render_template("tasks.html", tasks=mongo.db.tasks.find())


# @app.route('/nineMinutes', methods=['GET', 'POST'])
# def nineMinutes():
#     if request.method == 'GET':
#         return render_template('nineMinutes.html', nine_minutes=mongo.db.nineMinutes.find())
#     else:
#         insert_nineMinutes = mongo.db.nineMinutes
#         insert_nineMinutes.insert_one(request.form.to_dict())
#         return redirect(url_for('index'))


# @app.route('/nineMinutesUpdate', methods=['GET', 'POST'])
# def nineMinutesUpdate():
#     if request.method == 'GET':
#         return render_template('nineMinutesUpdate.html', nine_minutes=mongo.db.nineMinutes.find())
#     else:
#         insert_nineMinutes = mongo.db.nineMinutes
#         insert_nineMinutes.insert_one(request.form.to_dict())
#