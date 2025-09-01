# Foster Rae
# 02/09/2024
# Entry point

import pygame

# Setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

# Main Loop
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white") # Clear frame
    
    # Render here
    
    pygame.display.flip() # Update Frame
    clock.tick(60)

pygame.quit()
    