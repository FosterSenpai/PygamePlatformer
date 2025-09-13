import pygame
import json
import os
import time

class Player:
    def __init__(self, save_file_path=None) -> None:
        # Load default starting character stats
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
        self.score = data['score']
        self.hp = data['hp']
        self.speed = data['speed']
    
    def save_to_json(self) -> None:
        # Get/Create save directory
        current_dir = os.path.dirname(__file__)
        save_dir = os.path.join(current_dir, '../../data/saves')
        os.makedirs(save_dir, exist_ok=True)
        
        # Store player data in dict and convert to json
        data = {
            "score": self.score,
            "hp": self.hp,
            "speed": self.speed
        }
        # Build save path from timestamp
        time_stamp = time.strftime("%Y%m%d-%H%M%S")
        file_name = f"save_{time_stamp}.json"
        save_path = os.path.join(save_dir, file_name)
        
        # Store data in json file
        with open(save_path, "w") as f:
            json.dump(data, f)
            
    def handle_event(self, event: pygame.event.Event):
        # Movement input
        if event.type == pygame.KEYDOWN:
            # UI input
            if event.key == pygame.K_ESCAPE:
                return 'Pause'
            # Movement input
            elif event.key == pygame.K_w:
                pass # Not gonna be same as jump, maybe fall slower?
            elif event.key == pygame.K_a:
                pass # Move left
            elif event.key == pygame.K_s:
                pass # Move down
            elif event.key == pygame.K_d:
                pass # Move right
            elif event.key == pygame.K_SPACE:
                pass # Jump
            elif event.key == pygame.K_LSHIFT:
                pass # Dash
            return 'Moving'
        
        return None
