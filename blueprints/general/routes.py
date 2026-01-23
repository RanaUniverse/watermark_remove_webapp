"""
This is blueprints/general/routes.py
Here i will try to keep the basics things of the webpage
"""

from pathlib import Path


from flask import (
    render_template,
    Blueprint,
    abort,
    send_file,
)

folders_path = Path("files_and_folders")

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


@general_bp.route("/image")
def image():
    return send_file(
        "demo.png",
        mimetype="image/png",
    )


@general_bp.app_errorhandler(404)
def bp_404(e):
    return (
        render_template(
            "404.html",
            error_message=e.description,
        ),
        404,
    )


# Song and image below is for testing purspose only


@general_bp.route("/download_song")
def download_song():
    file_path = folders_path / "B He gobinda He radhe Rana Universe.mp3"
    if not file_path.exists():
        abort(
            code=404,
            description="song not found",
        )

    return send_file(
        file_path,
        mimetype="audio/mpeg",
        as_attachment=True,
        download_name="bhe_gobinda_he_radhe.mp3",
    )


@general_bp.route("/download_image")
def download_image():
    file_path = folders_path / "linux_logo.png"
    if not file_path.exists():
        abort(
            code=404,
            description="Image not found",
        )
    return send_file(
        path_or_file=file_path,
    )
