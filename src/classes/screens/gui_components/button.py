# Foster Rae
# 12/09/2025
# A simple button, changes colour on hover, detects clicks.
import pygame

class Button:
    def __init__(self, name, pos, width, height, base_colour, hover_colour, font, display_text, border_radius=0) -> None:
        self.name = name  # Way to id button when handling events
        
        # Colours
        self._base_colour = base_colour
        self._hover_colour = hover_colour
        
        # Text
        self._font = font
        self._text = display_text
        
        # Position and shape
        self._pos = pos
        self._width = width
        self._height = height
        self._border_radius = border_radius
        self._rect = pygame.Rect(self._pos[0],self._pos[1], self._width, self._height)
        
    def check_hover(self) -> bool:
        return False
        

        