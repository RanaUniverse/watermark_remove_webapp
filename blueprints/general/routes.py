"""
This is blueprints/general/routes.py
Here i will try to keep the basics things of the webpage
"""

from flask import render_template, Blueprint


general_bp = Blueprint(
    name="general_bp",
    import_name=__name__,
    template_folder="templates",
)


@general_bp.route("/")
def index():
    return render_template("general/index.html")


@general_bp.route("/help")
def help_page():
    return render_template("general/help_page.html")


@general_bp.route("/about")
def about_page():
    return render_template("general/about_page.html")
