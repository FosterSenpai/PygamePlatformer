import pygame
from ..levels.level_1 import Level1

class PlayScreen:
    def __init__(self, screen, player) -> None:
        # Screen Setup
        self._screen = screen
        self._bg_colour = (0,0,0)
        self._current_level = Level1()
        self._player = player
        
    def draw(self) -> None:
        # Prepare Screen
        self._screen.fill(self._bg_colour)
        pygame.display.set_caption(f"Platformer: {self._current_level.name}")
        
    def udpate(self) -> None:
        pass
    
    def handle_event(self, event):
        # Send events to be handled by player, check for 'Pause' response.
        player_result = self._player.handle_event(event)
        if player_result == "Pause":
            return player_result