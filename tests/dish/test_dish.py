from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish("Lasanha", 25.90)
    assert dish.name == "Lasanha"
    assert hash(dish) == hash(Dish("Lasanha", 25.90))
    assert hash(dish) != hash(Dish("Lasanha de Frango", 25.90))
    assert dish == dish
    assert dish != Dish("Lasanha de Frango", 25.90)

    assert repr(dish) == "Dish('Lasanha', R$25.90)"

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("tomate")
    dish.add_ingredient_dependency(ingredient1, 15)
    dish.add_ingredient_dependency(ingredient2, 10)
    assert dish.recipe.get(ingredient1) == 15
    assert dish.recipe.get(ingredient2) == 10

    assert dish.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert dish.get_ingredients() == {ingredient1, ingredient2}

    assert isinstance(dish, Dish)

    with pytest.raises(TypeError):
        Dish("Lasanha", "invalid_price")

    with pytest.raises(ValueError):
        Dish("Lasanha", -10.0)
