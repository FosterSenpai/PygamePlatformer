import pygame
from ..levels.level_1 import Level1
from .gui_components.button import Button
import config

class PlayScreen:
    def __init__(self, screen, player) -> None:
        # Screen Setup
        self._screen = screen
        self._bg_colour = (0,0,0)
        self._current_level = Level1()
        self._player = player
        self.paused = False
        
        # Pause buttons setup
        self._button_width = 200
        self._button_height = 50
        self._button_text_size = 30
        self._button_spacing = config.WINDOW_HEIGHT // 10
        self._pause_buttons = [
            Button(name="Resume",
                   pos= (config.WINDOW_WIDTH // 2 - self._button_width // 2, config.WINDOW_HEIGHT // 2 - 100),
                   width= self._button_width, height= self._button_height,
                   base_colour= (177, 177, 177), hover_colour=(200, 200, 200),
                   font= pygame.font.Font(None, self._button_text_size),
                   text='Resume', text_colour='white',
                   border_radius=3),
            Button(name="Options",
                   pos= (config.WINDOW_WIDTH // 2 - self._button_width // 2, config.WINDOW_HEIGHT // 2 - 100 + self._button_spacing),
                   width= self._button_width, height= self._button_height,
                   base_colour= (177, 177, 177), hover_colour=(200, 200, 200),
                   font= pygame.font.Font(None, self._button_text_size),
                   text='Options', text_colour='white',
                   border_radius=3),
            Button(name="MainMenu",
                   pos= (config.WINDOW_WIDTH // 2 - self._button_width // 2, config.WINDOW_HEIGHT // 2 - 100 + (self._button_spacing * 2)),
                   width= self._button_width, height= self._button_height,
                   base_colour= (177, 177, 177), hover_colour=(200, 200, 200),
                   font= pygame.font.Font(None, self._button_text_size),
                   text='Main Menu', text_colour='white',
                   border_radius=3)
        ]
        
    def draw(self) -> None:
        # Prepare Screen
        self._screen.fill(self._bg_colour)
        pygame.display.set_caption(f"Platformer: {self._current_level.name}")
        self._player.draw(self._screen)
        
        if self.paused:
            # Draw pause overlay
            for button in self._pause_buttons:
                button.draw(self._screen)
        
    def update(self) -> None:
        if not self.paused:
            self._player.update()
    
    def handle_event(self, event):
        if not self.paused: # Play screen events (Player, UI)
            # Player event responses
            player_result = self._player.handle_event(event)
            if player_result == "Pause":
                self.paused = not self.paused
                print('pause')
                
        else: # Handle pause overlay
            # Key inputs
            player_result = self._player.handle_event(event)
            if player_result == "Pause":
                self.paused = not self.paused
            # Buttons
            for button in self._pause_buttons:
                button.check_hover(pygame.mouse.get_pos())
                clicked = button.check_click(event)
                if clicked:
                    # Resume button handled here, rest handled by screen manager.
                    if button.name == "Resume":
                        self.paused = False
                    else:
                        return button.name