import pygame
from creatures.player import Player

class GameManager:
    def __init__(self) -> None:
        self.running = True
        self.player = None
        
    def update(self, delta_time) -> None:
        pass
    
    def set_player(self, player):
        self.player = player
