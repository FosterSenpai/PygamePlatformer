import pygame
from ..creatures.player import Player

class GameManager:
    def __init__(self) -> None:
        self.running = True
        self.player = None
        
    def update(self, delta_time) -> None:
        pass
    
    def create_new_player(self):
        self.player = Player()

    def load_player_from_file(self, save_file_path):
        self.player = Player(save_file_path)