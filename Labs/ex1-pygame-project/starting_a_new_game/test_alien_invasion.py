import pytest
import pygame
from unittest.mock import Mock, patch
from alien_invasion import AlienInvasion
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pygame.pkgdata")

@pytest.fixture
def game():
    return AlienInvasion()

@pytest.fixture
def mock_pygame_event():
    return Mock(spec=pygame.event.Event)

def test_keydown_right(game, mock_pygame_event):
    mock_pygame_event.type = pygame.KEYDOWN
    mock_pygame_event.key = pygame.K_RIGHT

    with patch('pygame.event.get', return_value=[mock_pygame_event]):
        game._check_events()

    assert game.ship.moving_right == True
    assert game.ship.moving_left == False

def test_keydown_left(game, mock_pygame_event):
    mock_pygame_event.type = pygame.KEYDOWN
    mock_pygame_event.key = pygame.K_LEFT

    with patch('pygame.event.get', return_value=[mock_pygame_event]):
        game._check_events()

    assert game.ship.moving_right == False
    assert game.ship.moving_left == True

def test_keyup_right(game, mock_pygame_event):
    # First, set moving_right to True
    game.ship.moving_right = True

    mock_pygame_event.type = pygame.KEYUP
    mock_pygame_event.key = pygame.K_RIGHT

    with patch('pygame.event.get', return_value=[mock_pygame_event]):
        game._check_events()

    assert game.ship.moving_right == False

def test_keyup_left(game, mock_pygame_event):
    # First, set moving_left to True
    game.ship.moving_left = True

    mock_pygame_event.type = pygame.KEYUP
    mock_pygame_event.key = pygame.K_LEFT

    with patch('pygame.event.get', return_value=[mock_pygame_event]):
        game._check_events()

    assert game.ship.moving_left == False

def test_quit_event(game, mock_pygame_event):
    mock_pygame_event.type = pygame.QUIT

    with patch('pygame.event.get', return_value=[mock_pygame_event]):
        game._check_events()

    assert game.running == False