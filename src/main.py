# Foster Rae
# 02/09/2024
# Entry point

import pygame
from classes.player import Player

# Setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
player = Player(screen)
delta_time = 0

# Main Loop
while running:
    
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white") # Clear frame
    
    # Rendering
    player.draw()
    
    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player._position.y -= player._max_speed * delta_time
    if keys[pygame.K_s]:
        player._position.y += player._max_speed * delta_time
    if keys[pygame.K_a]:
        player._position.x -= player._max_speed * delta_time
    if keys[pygame.K_d]:
        player._position.x += player._max_speed * delta_time 
    
    pygame.display.flip() # Update Frame
    delta_time = clock.tick(60) / 1000

pygame.quit()
    