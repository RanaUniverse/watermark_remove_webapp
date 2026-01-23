"""
This is my main.py to run my website.
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from flask import Flask


from blueprints.color_generate.routes import color_generate_bp
from blueprints.games.routes import games_bp
from blueprints.general.routes import general_bp
from blueprints.profile.routes import profile_bp

from utils.config_settings import FLASK_DEBUG, FLASK_HOST, FLASK_PORT, SECRET_KEY


app = Flask(
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
)

app.config["SECRET_KEY"] = SECRET_KEY


app.register_blueprint(color_generate_bp, url_prefix="/color")
app.register_blueprint(games_bp, url_prefix="/games")
app.register_blueprint(general_bp)
app.register_blueprint(profile_bp, url_prefix="/profile")


if __name__ == "__main__":
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG,
    )
