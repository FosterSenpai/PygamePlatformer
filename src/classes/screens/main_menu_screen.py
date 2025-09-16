import pygame
from .gui_components.button import Button
import config

class MainMenuScreen:
    def __init__(self, screen) -> None:
        
        # Screen Setup
        self._screen = screen
        self._bg_image = None
        self._bg_colour = (0,0,0)
        
        # Button Setup
        self._button_width = 200
        self._button_height = 50
        self._button_text_size = 30
        self._buttons = [
            Button(name="Start",
                   pos= (config.WINDOW_WIDTH // 2 - self._button_width // 2, config.WINDOW_HEIGHT // 2 - 100),
                   width= self._button_width, height= self._button_height,
                   base_colour= (177, 177, 177), hover_colour=(200, 200, 200),
                   font= pygame.font.Font(None, self._button_text_size),
                   text='Start Game', text_colour='white',
                   border_radius=3)
        ]
        
    def draw(self) -> None:
        # Prepare screen
        self._screen.fill(self._bg_colour)
        pygame.display.set_caption("Platformer: Main Menu")
        
        # Draw buttons
        for button in self._buttons:
            button.draw(self._screen)
        
    def update(self) -> None:
        pass
            
    def handle_event(self, event):
        """Handle events for main menu (buttons etc.), output component name to screen
        manager for logic to be handled there.
        Args:
            event (pygame.event): The pygame event to be handled
        Returns:
            str: Name of component interacted with in event, or None if no component used.
        """
        # Handle Buttons
        for button in self._buttons:
            # Change color on hover.
            button.check_hover(pygame.mouse.get_pos())
            # Output button name when clicked.
            # Handle logic based on button name in screen manager.
            clicked = button.check_click(event)
            if clicked:
                return button.name
        return None
            
    