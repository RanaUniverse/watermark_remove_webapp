"""
This is the blueprints/color_generate/routes.py file
i will want to have this will make a image in pillow and send the image back to ser in the html
"""

from flask import Blueprint, render_template, Response
from utils.image_generation import generate_color_image
import io

color_generate_bp = Blueprint(
    name="color_generate_bp",
    import_name=__name__,
    template_folder="templates",
)


@color_generate_bp.route("/")
def index():
    return render_template("color/index.html")


@color_generate_bp.route("/image")
def generate_image():
    image = generate_color_image()
    image.show()

    img_io = io.BytesIO()
    image.save(img_io, "PNG")
    img_io.seek(0)

    return Response(img_io, mimetype="image/png")
