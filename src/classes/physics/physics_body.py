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
        # Using inverse mass in force calculations avoids div by 0 and reduces need for division,
        # can just multiply by inverse_mass instead of div by mass.
        self.inverse_mass = 0.0 if self.mass == float("inf") else 1.0 / self.mass # Set to 0 for static moving objects (moving platforms etc.) and 1 for dynamic moving objects
        self.forces = pygame.math.Vector2(0.0, 0.0) # Accumulated forces to be applied
        self.on_ground = False
        
        # Environment
        self.gravity = gravity
        self.linear_damping = max(0.0, min(linear_damping, 0.99)) # Keep within 0-0.99 damping, 100% damping inverts velocity
        
    def add_force(self, force_x: float, force_y: float) -> None:
        # Add force to accumulated forces for this frame, cleared when forces applied.
        self.forces.x += force_x
        self.forces.y += force_y
    
    def apply_force(self, delta_time: float) -> None:
        # Apply accumulated forces to physics body.
        
        # If body is 'static' just clear forces without applying.
        if self.inverse_mass == 0.0:
            self.forces.x = self.forces.y = 0
            return
        
        # Add gravity
        self.forces.y += self.mass * self.gravity
        
        # Acceleration (a = F / m)
        acceleration_x = self.forces.x * self.inverse_mass
        acceleration_y = self.forces.y * self.inverse_mass
        
        # Velocity (v = v + a * dt)
        self.velocity.x += acceleration_x * delta_time
        self.velocity.y += acceleration_y * delta_time
        
        # Position = (x = x + v * dt)
        self.position.x += self. velocity.x * delta_time
        self.position.y += self. velocity.y * delta_time
        
        # Damping (Slow down velocity over time)
        if self.linear_damping > 0.0: # Dont do calculations if no damping
            self.velocity.x *= (1.0 - self.linear_damping)
            self.velocity.y *= (1.0 - self.linear_damping)
            
        # Clear forces
        self.forces.x, self.forces.y = 0.0 ,0.0
        
    def apply_impulse(self, impulse_x: float, impulse_y: float) -> None:
        # Instantly apply a force
        if self.inverse_mass > 0.0: # Dont apply to 'static' objects
            self.velocity.x += impulse_x * self.inverse_mass
            self.velocity.y += impulse_y * self.inverse_mass
    
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
            
            