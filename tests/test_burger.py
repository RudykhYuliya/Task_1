from unittest.mock import Mock

import pytest

from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient(self, burger, mock_first_ingredient):
        burger.add_ingredient(mock_first_ingredient)
        assert burger.ingredients == [mock_first_ingredient]

    def test_remove_ingredient(self, burger, mock_first_ingredient, mock_second_ingredient):
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_second_ingredient]

    @pytest.mark.parametrize('index, new_index, expected_order', [
        (0, 2, (1, 2, 0)),
        (2, 0, (2, 0, 1)),
    ])
    def test_move_ingredient(
        self, burger, mock_first_ingredient, mock_second_ingredient, index, new_index, expected_order,
    ):
        third_ingredient = Mock(spec=Ingredient)
        ingredients = [mock_first_ingredient, mock_second_ingredient, third_ingredient]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        burger.move_ingredient(index, new_index)
        assert burger.ingredients == [ingredients[position] for position in expected_order]

    def test_get_price(self, burger, mock_bun, mock_first_ingredient, mock_second_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        assert burger.get_price() == 330

    def test_get_receipt(self, burger, mock_bun, mock_first_ingredient, mock_second_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        assert burger.get_receipt() == (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== black bun ====)\n'
            '\n'
            'Price: 330'
        )
