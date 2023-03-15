import os
# importing flask class
from flask import Flask, render_template

# creating instance of flask class and storing in var
# (__name__) is name of apps module/package
# so flask knows where to look for static templates/files
app = Flask(__name__)


# @app.route decorator, wrap func
# "/" = root directory, when we browse this index is called
@app.route("/")
def index():
    return render_template("index.html")


# "__main__" is name of default module in Python, first one we run
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
