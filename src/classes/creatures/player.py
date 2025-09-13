import pygame
import json

class Player:
    def __init__(self, name="", save_file=None) -> None:
        # Load default starting character stats
        self.name = name
        self.score = 0
        self.hp = 100
        self.speed = 10
    
    def load_from_json(self, save_file) -> None:
        pass
    
    def save_to_json(self) -> str:
        return json.dumps({"empty": "empty"})