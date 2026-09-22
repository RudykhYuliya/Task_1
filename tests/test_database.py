from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestDatabase:
    def test_available_buns(self, database):
        buns = database.available_buns()
        assert [(bun.get_name(), bun.get_price()) for bun in buns] == [
            ('black bun', 100),
            ('white bun', 200),
            ('red bun', 300),
        ]

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert [
            (ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
            for ingredient in ingredients
        ] == [
            (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            (INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
            (INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
            (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
            (INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
            (INGREDIENT_TYPE_FILLING, 'sausage', 300),
        ]
