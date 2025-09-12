import pygame

class GameManager:
    def __init__(self) -> None:
        self.running = True
        self.clock = pygame.time.Clock()
        
    def update(self) -> None:
        self.clock.tick(60)
        
