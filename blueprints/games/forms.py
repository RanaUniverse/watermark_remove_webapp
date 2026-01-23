"""
This is the part where i will make the csrf token related flask-wtf forms defined
blueprints/games/forms.py
"""

from flask_wtf import FlaskForm  # type: ignore

from wtforms import SubmitField, RadioField, StringField, HiddenField

from wtforms.validators import DataRequired


class MathMCQForm(FlaskForm):
    """
    This is incomplete ...
    """

    answer = RadioField(
        label="Choose The Correct Answer",
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit Answer Here")


class MathAnswerForm(FlaskForm):
    """
    I use this to make the html form in jinja
    so that it will easy to handle and generate data
    """

    question_id = HiddenField(
        # render_kw={"id": "math-question-id"},
    )
    answer = StringField(
        label="Write The Answer",
        validators=[DataRequired()],
        render_kw={
            "placeholder": "Write Here",
            "size": "50",
            "id": "answer_field",
        },
    )
    submit = SubmitField(label="Submit Your Answer")
