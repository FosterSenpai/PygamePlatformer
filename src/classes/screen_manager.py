import pygame
from .screens.main_menu_screen import MainMenuScreen
import config

class ScreenManager:
    def __init__(self, game_manager) -> None:
        # Screen 
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH,config.WINDOW_HEIGHT))
        self._current_screen = MainMenuScreen(self.screen)
        
        # Game Data
        self._game_manager = game_manager

    def update(self, delta_time) ->None:
        pass

    def handle_event(self, event) -> None:
        """Handle screen specific events for things like screen changing.
        Args:
            event (pygame.event): The pygame event to handle.
        """
        # Main menu event handling
        if isinstance(self._current_screen, MainMenuScreen):
            result = self._current_screen.handle_event(event)
            if result == "Start": # Start Game Button
                print(result) # TODO: Link game screen
                
    
    def draw(self) -> None:
        self._current_screen.draw()