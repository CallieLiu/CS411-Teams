import pytest

from meal_max.models.battle_model import BattleModel
from meal_max.models.kitchen_model import Meal


@pytest.fixture()
def battle_model():
    """Fixture to provide a new instance of BattleModel for each test."""
    return BattleModel()

@pytest.fixture
def mock_update_meal_stats(mocker):
    """Mock the update_meal_stats function for testing purposes."""
    return mocker.patch("meal_max.models.battle_model.update_meal_stats")

"""Fixtures providing sample songs for the tests."""
@pytest.fixture
def sample_meal1():
    return Meal(1, 'Spaghetti', 'Italian', 15, 'MED')

@pytest.fixture
def sample_meal2():
    return Meal(2, 'Sushi', 'Japanese', 8, 'HIGH')

@pytest.fixture
def sample_battle1(sample_meal1):
    return [sample_meal1]

@pytest.fixture
def sample_battle2(sample_meal1, sample_meal2):
    return [sample_meal1, sample_meal2]