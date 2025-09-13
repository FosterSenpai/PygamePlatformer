import pygame
from ..levels.level_1 import Level1

class PlayScreen:
    def __init__(self, screen) -> None:
        # Screen Setup
        self._screen = screen
        self._bg_colour = (0,0,0)
        self._current_level = Level1()
        
    def draw(self) -> None:
        # Prepare Screen
        self._screen.fill(self._bg_colour)
        pygame.display.set_caption(f"Platformer: {self._current_level.name}")
        
    def udpate(self) -> None:
        pass
    
    def handle_event(self, event):
        pass