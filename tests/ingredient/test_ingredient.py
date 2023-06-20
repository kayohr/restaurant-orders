from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    presunto = Ingredient("presunto")
    massa_de_lasanha = Ingredient("massa de lasanha")

    assert presunto.name == "presunto"
    assert presunto.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert massa_de_lasanha.name == "massa de lasanha"
    assert massa_de_lasanha.restrictions == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
    }

    assert hash(presunto) == hash("presunto")
    assert hash(massa_de_lasanha) == hash("massa de lasanha")

    assert presunto == Ingredient("presunto")
    assert massa_de_lasanha == Ingredient("massa de lasanha")

    assert repr(presunto) == "Ingredient('presunto')"
    assert repr(massa_de_lasanha) == "Ingredient('massa de lasanha')"
