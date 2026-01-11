"""
This is my main.py to run my website.
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from flask import Flask


from blueprints.general.routes import general_bp
from blueprints.profile.routes import profile_bp


from utils.config_settings import FLASK_DEBUG, FLASK_HOST, FLASK_PORT


app = Flask(
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
)

app.register_blueprint(general_bp)
app.register_blueprint(profile_bp, url_prefix="/profile")


if __name__ == "__main__":
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG,
    )
