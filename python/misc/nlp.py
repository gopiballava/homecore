
from fuzzywuzzy import fuzz
import inflect

STARCH_LIST = [
    "rice",
    "pieorogie",
    "potato",
    "bread",
    "muffin",
    "pasta",
    "spaghetti",
    "linguine",
    "fettucine",
    "noodle",
    "risotto",
    "oatmeal",
    "sandwich",
    "pizza",
    "hoagie",
]

p = inflect.engine()

STARCH_LIST = STARCH_LIST + [p.plural(x) for x in STARCH_LIST]


def is_starch(food_name):
    matches = [fuzz.token_set_ratio(x, food_name) for x in STARCH_LIST]
    print(STARCH_LIST)
    print(food_name, matches)
    return max(matches) > 80

