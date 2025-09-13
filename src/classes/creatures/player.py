import pygame
import json
import os

class Player:
    def __init__(self, name="", save_file_path=None) -> None:
        # Load default starting character stats
        self.name = name
        self._save_count = 0
        self.score = 0
        self.hp = 100
        self.speed = 10
        # Update default stats with those from save file
        if save_file_path is not None:
            self.load_from_json(save_file_path)
    
    def load_from_json(self, save_file_path) -> None:
        # Load file as dict
        with open(save_file_path, "r") as f:
            data = json.load(f)
        
        # Update member variables from json
        self.name = data['name']
        self._save_count = data['save_count']
        self.score = data['score']
        self.hp = data['hp']
        self.speed = data['speed']
    
    def save_to_json(self) -> None:
        # Get/Create save directory
        current_dir = os.path.dirname(__file__)
        save_dir = os.path.join(current_dir, '../../data/saves')
        os.makedirs(save_dir, exist_ok=True)
        
        # Store player data in dict and convert to json
        self._save_count += 1
        data = {
            "name": self.name,
            "save_count": self._save_count,
            "score": self.score,
            "hp": self.hp,
            "speed": self.speed
        }
        # Build save path from name and save no.
        save_path = os.path.join(save_dir, f"{data['name']}SAVE{data['save_count']}")
        
        # Store data in json file
        with open(save_path, "w") as f:
            json.dump(data, f)