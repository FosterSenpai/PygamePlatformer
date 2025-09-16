import pygame
import json
import os
import time
import config

class Player:
    def __init__(self, save_file_path=None) -> None:
        # Load default starting character stats
        self.score = 0
        self.hp = 100
        self.speed = 10
        
        # Position
        self.x = config.WINDOW_WIDTH //2
        self.y = config.WINDOW_HEIGHT //2
        
        # Sprite setup
        self._spritesheet_path = os.path.join(config.SPRITE_PATH,"player")
        self._sprites = self.load_sprites()
        self._current_action = "IDLE"
        self._current_spritesheet = self._sprites[self._current_action]
        self._frame_index = 0
        self._is_facing_left = False
        self._frame_height = 96
        self._frame_width = 96
        self._current_frame = self.get_current_frame()

        # Animation timing
        self._animation_timer = 0
        self._base_animation_speed = 0.05 # Time between frame changes (seconds)
        
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
    
    def load_sprites(self):
        actions = ["AIR ATTACK", "ATTACk 1", "ATTACk 2", "ATTACk 3", "CLIMBING", "DASH", "DEATH",
                   "DEFEND", "HEALING NO EFFECT", "HEALING", "HURT", "IDLE", "JUMP FALL", "JUMP START",
                   "JUMP TRANSITION", "JUMP", "RUN", "SPECIAL ATTACK", "THROW", "WALK", "WALL CONTACT",
                   "WALL JUMP", "WALL SLIDE"]
        sprites = {}
        # Store each action and corresponding spritesheet in dict.
        for action in actions:
            path = os.path.join(self._spritesheet_path, f"{action}.png")
            sprites[action] = pygame.image.load(path).convert_alpha()
        return sprites
    
    def update(self, delta_time=1/60):
        # Update current sprite sheet for action.
        self._current_spritesheet = self._sprites[self._current_action]
        self.update_animation(delta_time)
        self._current_frame = self.get_current_frame()
    
    def get_current_frame(self):
        # Rectangle for cutting out frame
        frame_rect = pygame.Rect(self._frame_index * self._frame_width, 0, self._frame_width, self._frame_height)
        frame = self._current_spritesheet.subsurface(frame_rect)
        
        # Flip frame if facing left
        if self._is_facing_left:
            frame = pygame.transform.flip(frame, True, False)
        
        return frame
        
    
    def draw(self, surface):
        surface.blit(self._current_frame, (self.x, self.y))
        
    def update_animation(self, delta_time):
        # Calculate number of frames in sheet
        sheet_width = self._current_spritesheet.get_width()
        num_frames = sheet_width // self._frame_width

        # Animation speed  tied to player speed
        # Higher player speed, lower time between frames
        animation_speed = self._base_animation_speed / max(1, self.speed / 10)
        self._animation_timer += delta_time # Increment timer
        # If timer hits animation speed increment frame and reset timer
        if self._animation_timer >= animation_speed:
            self._animation_timer = 0
            self._frame_index += 1
            # Reset after last frame
            if self._frame_index >= num_frames:
                self._frame_index = 0