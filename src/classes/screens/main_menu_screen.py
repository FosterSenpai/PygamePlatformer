import pygame

class MainMenuScreen:
    def __init__(self, screen) -> None:
        self.BG_IMAGE = None
        self.BG_COLOUR = (0,0,0)
        
        self._screen = screen
        
    def draw(self) -> None:
        # Update screen state
        self.update()
        # Setup screen
        self._screen.fill(self.BG_COLOUR)
        pygame.display.set_caption("Main Menu")
        
    def update(self) -> None:
        pass