import pygame
from .screens.main_menu_screen import MainMenuScreen
from .game_manager import GameManager
import config

class ScreenManager:
    def __init__(self, game_manager) -> None:
        # Screen 
        pygame.init()
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH,config.WINDOW_HEIGHT))
        self._current_screen = MainMenuScreen(self.screen)
        
        # Game Data
        self._game_manager = game_manager
        self.running = self._game_manager.running

    def update(self) ->None:
        # Update Game State
        self._game_manager.update()

    def handle_event(self, event) -> None:
        """Handle general events and screen specific events for things like screen changing.
        Args:
            event (pygame.event): The pygame event to handle.
        """
        # Window quit button
        if event.type == pygame.QUIT:
            self.running = False
            
        # - Screen Specific Event Handling -
        # Main menu event handling
        if isinstance(self._current_screen, MainMenuScreen):
            result = self._current_screen.handle_event(event)
            if result == "Start": # Start Game Button
                pass # TODO: Link game screen
                
    
    def draw(self) -> None:
        self._current_screen.draw()
        pygame.display.update()

    
    def run(self) -> None:
        """Run the main game loop."""
        while self.running:
            # Update Screen State
            self.update()
            # Handle Events
            for event in pygame.event.get():
                self.handle_event(event)
            # Draw Screen
            self.draw()
        pygame.quit()