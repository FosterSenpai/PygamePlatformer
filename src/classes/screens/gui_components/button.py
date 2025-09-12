# Foster Rae
# 12/09/2025
# A simple button, changes colour on hover, detects clicks.
import pygame

class Button:
    def __init__(self, name, pos, width, height, base_colour, hover_colour, font, text, text_colour, border_radius=0) -> None:
        self.name = name  # Way to id button when handling events
        
        # Colours
        self._base_colour = base_colour
        self._hover_colour = hover_colour
        self._current_colour = base_colour
        self._text_colour = text_colour
        
        # Text
        self._font = font
        self._text = text
        self._text_surface = self._font.render(self._text, True, self._text_colour)
        
        # Position and shape
        self._pos = pos
        self._width = width
        self._height = height
        self._border_radius = border_radius
        self._rect = pygame.Rect(self._pos[0], self._pos[1], self._width, self._height)
        self._text_rect = self._text_surface.get_rect(self._rect.center) # Center inside button rect
        
    def check_hover(self, mouse_pos) -> bool:
        mouse_x, mouse_y = mouse_pos
        
        # Change colour if mouse colliding with button rect.
        if self._rect.collidepoint(mouse_x, mouse_y):
            self._current_colour = self._hover_colour
            return True
        else:
            self._current_colour = self._base_colour
            return False
        
    def check_click(self, event) -> bool:
        # Return true if click event happened inside button rect.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(event.pos):
                return True
        return False
    
    def draw(self, screen) -> None:
        # Draw button rectangle
        pygame.draw.rect(screen, self._current_colour, self._rect, self._border_radius)
        # Draw button text
        screen.blit(self._text_surface,self._text_rect)
        

        