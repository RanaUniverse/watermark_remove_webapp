"""
This is the file of blueprints/profile/routes.py
Here i want to make the profile for now i want to
do so that profile related things will stay here
"""

from flask import Blueprint, render_template


profile_bp = Blueprint(
    name="profile_bp",
    import_name=__name__,
    template_folder="templates",
)


@profile_bp.route("/")
def index():
    return render_template(
        template_name_or_list="profile_index_page.html",
    )
