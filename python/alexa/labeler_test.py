
from .labeler import Labeler

from flask_ask import statement, question

statement_type = type(statement(""))

question_type = type(question(""))


def test_ok():
    assert True


def test_is_yes():
    lab = Labeler()
    assert lab._is_yes("yes")
    assert lab._is_yes("correct")
    assert lab._is_yes("yup")
    assert not lab._is_yes("no")


def test_basic_flow():
    lab = Labeler()
    assert type(lab.handle_statement("french baguette sandwich")) == question_type
    assert lab.potential_food is "french baguette sandwich"
    assert type(lab.handle_statement("yes")) == question_type
    assert lab.potential_food is None


def test_first_yes():
    # If we say "yes" when there is nothing pending...
    lab = Labeler()
    assert type(lab.handle_statement("yes")) == question_type
    assert lab.potential_food is None