import os
# import json library
import json
# importing flask class
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


# creating instance of flask class and storing in var
# (__name__) is name of apps module/package
# so flask knows where to look for static templates/files
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# @app.route decorator, wrap func
# "/" = root directory, when we browse this index is called
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # open json file as read only, assign contents to json_data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # needs to be indented to ( point
    return render_template("about.html",
                           page_title="About",
                           company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# "__main__" is name of default module in Python, first one we run
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
