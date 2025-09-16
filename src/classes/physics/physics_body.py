# Foster Rae
# 19/09/2025
# Class to handle physics for an object. Handles applying and calculating forces.
import pygame

class PhysicsBody:
    def __init__(
        self,
        mass: float = 100.0,
        gravity: float = 9.8,
        position: tuple[float, float] = (0.0, 0.0),
        velocity: tuple[float, float] = (0.0, 0.0),
        linear_damping: float = 0.3 # Velocity slow down over time
        ) -> None:
        # Physics body
        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(velocity)
        self.mass = mass
        self.forces = pygame.math.Vector2(0.0, 0.0) # Accumulated forces to be applied
        self.on_ground = False
        
        # Environment
        self.gravity = gravity
        self.linear_damping = max(0.0, min(linear_damping, 0.99)) # Keep within 0-0.99 damping, 100% damping inverts velocity
        
    def add_force(self, force_x: float, force_y: float) -> None:
        # Add force to accumulated forces for this frame.
        pass
    
    def apply_force(self) -> None:
        # Apply accumulated forces to physics body.
        pass
    
    def add_impulse(self, impulse_x: float, impulse_y: float) -> None:
        # Instantly apply a force
        pass
    
    def set_position(self, x:float, y: float) -> None:
        self.position.x, self.position.y = x, y
    
    def set_velocity(self, velocity_x: float, velocity_y: float):
        self.velocity.x, self.velocity.y = velocity_x, velocity_y
        
    def clamp_velocity(self, max_velocity_x: float, max_velocity_y: float) -> None:
        # Clamp in both directions
        if max_velocity_x is not None:
            if self.velocity.x > max_velocity_x: self.velocity.x = max_velocity_x
            if self.velocity.x < -max_velocity_x: self.velocity.x = -max_velocity_x
        if max_velocity_y is not None:
            if self.velocity.y > max_velocity_y: self.velocity.y = max_velocity_y
            if self.velocity.y < -max_velocity_y: self.velocity.y = -max_velocity_y
            
            