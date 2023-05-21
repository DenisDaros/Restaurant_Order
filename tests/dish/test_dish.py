from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient, Restriction


value1 = 30.00
value2 = 50.00

# Req 2


def test_dish():
    dish = Dish("feijoada", value1)
    dish_copia = Dish("feijoada", value1)
    dish_diferent = Dish("churrasco", value2)
    bacon = Ingredient("bacon")
    dish.add_ingredient_dependency(bacon, 2)
    with pytest.raises(TypeError):
        Dish("feijoada", "value1")
    with pytest.raises(ValueError):
        Dish("feijoada", 0)
    assert dish.name == "feijoada"
    assert dish.price == value1
    assert hash(dish) == hash(dish_copia)
    assert hash(dish) != hash(dish_diferent)
    assert dish.__eq__(dish_copia) is True
    assert dish.__eq__(dish_diferent) is False
    assert repr(dish) == "Dish('feijoada', R$30.00)"
    assert dish.get_ingredients() == {Ingredient('bacon')}
    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT}
