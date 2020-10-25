import os
from flask import Flask, render_template
# to import pymongo
from flask_pymongo import PyMongo

# for env.py set up
if os.path.exists("env.py"):
    import env
# bson.json converts the mongo format to json for workability
from bson.json_util import dumps, loads
app = Flask(__name__)

# to set the DB and the URI
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
print(os.environ.get("MONGO_URI"))
# to set the mongo object
mongo = PyMongo(app)


# initialise Users database
@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.task.find())
    return render_template("tasks.html",tasks=tasks)

# # ADD tasks (C in CRUD -> Create/Add)
# @app.route("/add_task")
# def add_task():
#         return render_template("addtask.html", categories=mongo.db.categories.find())

# @app.route("/insert_task", methods=["POST"])
# def insert_task():
#         tasks = mongo.db.tasks
#         tasks.insert_one(request.form.to_dict())
#         return redirect(url_for("get_tasks"))


# # ADD categories (C in CRUD -> Create/Add)
# @app.route("/add_category")
# def add_category():
#         return render_template("addcategory.html")


# @app.route("/insert_category", methods=["POST"])
# def insert_category():
#         categories = mongo.db.categories
#         category_doc = {"category_name": request.form.get("category_name")}
#         categories.insert_one(category_doc)
#         return redirect(url_for("get_categories"))


# # VIEW categories (R in CRUD -> Read/View)
# @app.route("/get_categories")
# def get_categories():
#         return render_template("categories.html",
#         categories = mongo.db.categories.find())


# # EDIT tasks (U in CRUD -> Update/Edit)
# @app.route("/edit_task/<task_id>")
# def edit_task(task_id):
#         the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
#         all_categories = mongo.db.categories.find()
#         return render_template("edittask.html", task=the_task, categories=all_categories)

@app.route("/update_task/<task_id>", methods=["POST"])
def update_task(task_id):
        tasks = mongo.db.tasks
        tasks.update( {"_id": ObjectId(task_id)},
        {
                "task_name": request.form.get("task_name"),
                "category_name": request.form.get("category_name"),
                "task_description": request.form.get("task_description"),
                "due_date": request.form.get("due_date"),
                "is_urgent": request.form.get("is_urgent")
        })
        return redirect(url_for("get_tasks"))


# EDIT categories (U in CRUD -> Update/Edit)
@app.route("/edit_category/<category_id>")
def edit_category(category_id):
        return render_template("editcategory.html",
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)}))

@app.route("/update_category/<category_id>", methods=["POST"])
def update_category(category_id):
        categories = mongo.db.categories
        categories.update( {"_id": ObjectId(category_id)},
        {
                "category_name": request.form.get("category_name")
        })
        return redirect(url_for("get_categories"))


# DELETE tasks (D in CRUD -> Delete)
@app.route("/delete_task/<task_id>")
def delete_task(task_id):
        mongo.db.tasks.remove({"_id": ObjectId(task_id)})
        return redirect(url_for("get_tasks"))


# DELETE categories (D in CRUD -> Delete)
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        return redirect(url_for("get_categories"))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
