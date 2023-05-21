from src.models.ingredient import (Ingredient, restriction_map)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("queijo mussarela")
    ingredient_copia = Ingredient("queijo mussarela")
    ingredient_diferent = Ingredient("farinha")
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == restriction_map()["queijo mussarela"]
    assert hash(ingredient) == hash(ingredient_copia)
    assert hash(ingredient) != hash(ingredient_diferent)
    assert ingredient.__eq__(ingredient_copia) is True
    assert ingredient.__eq__(ingredient_diferent) is False
    assert repr(ingredient) == "Ingredient('queijo mussarela')"
