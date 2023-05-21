from src.models.ingredient import Ingredient
from src.models.dish import Dish
import pandas as pd
# Req 3


class MenuData:
    def __init__(self, source_path: str) -> None:
        df = pd.read_csv(source_path).itertuples(index=False)
        self.dishes = set()
        list = {}

        for name, price, ingredient, amount in df:
            dish = Dish(name, price)
            ingredient = Ingredient(ingredient)

            if name not in list:
                list[name] = dish
                self.dishes.add(dish)

            list[name].add_ingredient_dependency(ingredient, amount)
