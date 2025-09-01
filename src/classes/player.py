# Foster Rae
# 02/09/2025
# Class containing all direct player data, positional info, stats etc.

import pygame

class Player:
    def __init__(self, screen) -> None:
        self._sprite_size = 5
        self._max_speed = 10
        self._position = pygame.Vector2(screen.get_width()/2, screen.get_width()/2)
        self._screen = screen
        self._colour = "blue"
        
    def draw(self):
        pygame.draw.circle(self._screen, self._colour, self._position, float(self._sprite_size))