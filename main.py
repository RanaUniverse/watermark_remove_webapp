"""
This is my main.py to run my website.
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from flask import Flask, render_template


from utils.config_settings import FLASK_DEBUG, FLASK_HOST, FLASK_PORT


app = Flask(
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/help")
def help_page():
    return render_template("help_page.html")


@app.route("/about")
def about_page():
    return render_template("about_page.html")


if __name__ == "__main__":
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG,
    )
