import pytest
from unittest.mock import Mock, patch
import pygame
from ship import Ship

@pytest.fixture
def mock_ai_game():
    mock = Mock()
    mock.screen = Mock()
    mock.screen.get_rect.return_value = pygame.Rect(0, 0, 800, 600)
    return mock

@pytest.fixture
def ship(mock_ai_game):
    with patch('pygame.image.load') as mock_load:
        mock_image = Mock()
        mock_image.get_rect.return_value = pygame.Rect(0, 0, 50, 50)
        mock_load.return_value = mock_image
        return Ship(mock_ai_game)

def test_ship_initialization(ship, mock_ai_game):
    assert ship.screen == mock_ai_game.screen
    assert ship.rect.midbottom == mock_ai_game.screen.get_rect().midbottom
    assert ship.speed == 2.5
    assert ship.moving_right == False
    assert ship.moving_left == False

def test_ship_update_moving_right(ship):
    ship.moving_right = True
    initial_x = ship.x
    ship.update()
    assert ship.x > initial_x
    assert ship.rect.right <= ship.screen_rect.right

def test_ship_update_moving_left(ship):
    ship.moving_left = True
    ship.x = 100  # Start a bit to the right
    initial_x = ship.x
    ship.update()
    assert ship.x < initial_x
    assert ship.rect.left >= 0

def test_ship_update_not_moving(ship):
    initial_x = ship.x
    ship.update()
    assert ship.x == initial_x

def test_ship_update_right_boundary(ship):
    ship.moving_right = True
    ship.rect.right = ship.screen_rect.right
    ship.x = float(ship.rect.x)
    initial_x = ship.x
    ship.update()
    assert ship.x == initial_x

def test_ship_update_left_boundary(ship):
    ship.moving_left = True
    ship.rect.left = 0
    ship.x = float(ship.rect.x)
    initial_x = ship.x
    ship.update()
    assert ship.x == initial_x

def test_ship_blitme(ship):
    with patch.object(ship.screen, 'blit') as mock_blit:
        ship.blitme()
        mock_blit.assert_called_once_with(ship.image, ship.rect)