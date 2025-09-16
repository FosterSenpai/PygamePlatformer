import pygame
from .managers.game_manager import GameManager
from .managers.screen_manager import ScreenManager

class Game:
    def __init__(self) -> None:
        # Setup
        pygame.init()
        self._running = True
        self._clock = pygame.time.Clock()
        # Managers
        self._game_manager = GameManager()
        self._screen_manager = ScreenManager(self._game_manager)

    def update(self, delta_time) -> None:
        # Update game state
        self._game_manager.update(delta_time)
        self._running = self._game_manager.running
        
        # Update screen state
        self._screen_manager.update(delta_time)
    
    def run(self) -> None:
        """Run the main game loop."""
        while self._running:
            # Updates
            delta_time = self._clock.tick(60) / 1000.0
            self.update(delta_time)
            
            # Events
            for event in pygame.event.get():
                # Window quit button
                if event.type == pygame.QUIT:
                    self._game_manager.running = False
                    self._running = False

                self._screen_manager.handle_event(event)
                
            # Drawing
            self._screen_manager.draw()
            pygame.display.flip() # Updating here in case drawing from multiple locations.
        pygame.quit()