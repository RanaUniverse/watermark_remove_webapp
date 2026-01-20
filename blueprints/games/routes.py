"""
This is the blueprints/games/routes.py
Here i want to keep some mcq like brain power little game for users who open the webside
"""

import random


from flask import render_template, Blueprint


from blueprints.games.forms import MathAnswerForm
from blueprints.games.questions import math_questions


games_bp = Blueprint(
    name="games_bp",
    import_name=__name__,
    template_folder="templates",
)


@games_bp.route("/")
def index():
    return render_template("games/index.html")


@games_bp.route("/rana_learning", methods=["GET", "POST"])
@games_bp.route("/r", methods=["GET", "POST"])
def rana_learning():
    """
    This is learning for only
    This has not any use for now for just checking in temrinal
    """
    random_question = random.choice(math_questions)

    form = MathAnswerForm()
    print(form.csrf_token())  # type: ignore
    print(form.hidden_tag())  # type: ignore
    print(form.answer)
    print(form.answer(size=20, maxlength=50))
    print(form.answer.label)
    print(form.answer.data)
    print(form.answer.errors)
    print("RanaUniverse")
    print(form.submit)
    print(form.submit.label)
    print(form.submit.data)
    print(form.submit())

    # below is just made in mind that it will send get req for now
    return render_template(
        "games/math.html",
        form=form,
        question=random_question,
    )



@games_bp.route("/math", methods=["GET", "POST"])
def math_game():
    random_question = random.choice(math_questions)
    form = MathAnswerForm()
    options_placeholder: list[str] = random_question["options"]
    form.answer.render_kw["placeholder"] = f"Answers Hint: {options_placeholder}"
    return render_template(
        template_name_or_list="games/math_game.html",
        form=form,
        question=random_question,
    )


@games_bp.route("/word", methods=["GET", "POST"])
def word_game():
    return render_template("games/word_game.html")


@games_bp.route("/memory", methods=["GET", "POST"])
def memory_game():
    return render_template("games/memory_game.html")
