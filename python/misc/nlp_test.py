from .nlp import is_starch


def test_is_starch():
    assert is_starch("rice")
    assert is_starch("indian rice")
    assert is_starch("baked potato")
    assert is_starch("mashed potatoes")
    assert is_starch("english muffin")
    assert is_starch("fried rice")
    assert is_starch("spaghetti bolognese")
    assert not is_starch("palak paneer")
    assert not is_starch("hamburger")
