# Foster Rae
# 17/09/2025
# Player controller that uses turns input into forces using PhysicsBody class.

from ..physics.physics_body import PhysicsBody

class PlayerController:
    def __init__(self) -> None:
        self.max_speed = 420.0
        self.ground_friction = 12.0 # Change for different ground materials
        self.air_control_scale = 0.5
    
    def handle_input(self, event, player_physics_body: PhysicsBody, delta_time):
        # Use physics body from player to add/apply forces based on input.
        # Maybe better to pass just the key pressed and call this func only if event is keypress.
        pass
        