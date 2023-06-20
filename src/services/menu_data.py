# Req 3
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        dish_menu = {}

        with open(source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                dish_name = row[0]
                dish_price = float(row[1])
                ingredient_name = row[2]
                recipe_amount = int(row[3])

                if dish_name not in dish_menu:
                    dish_menu[dish_name] = Dish(dish_name, dish_price)

                ingredient = Ingredient(ingredient_name)
                dish_menu[dish_name].add_ingredient_dependency(
                    ingredient, recipe_amount
                )

        self.dishes.update(dish_menu.values())
