import pygame
import sys

pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing")


Image = pygame.image.load("Bob.png")


Image = pygame.transform.scale(Image,(500,400))


# Initial position and speed for the object
x_pos = 0
y_pos = HEIGHT // 2
speed = 10

bob_x = 0

bob_y = 0

bob_speed = 10 
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: UPDATE THE OBJECT'S POSITION (e.g., x_pos += speed)
    x_pos += speed
    
    bob_x += bob_speed
    
    if x_pos > WIDTH or x_pos < 0:
        speed = -speed
    if bob_x > WIDTH or bob_x < 0:
        bob_speed = -bob_speed
    
    
    

    # TODO: Fill the screen with white
    screen.fill((255,255,255))
    
    
    
    # TODO: DRAW THE MOVING OBJECT (e.g., a rectangle or circle)
    pygame.draw.rect(screen, (255, 251, 212), (x_pos,y_pos, 100,100))
    
        # TODO: DRAW THE MOVING OBJECT (e.g., a rectangle or circle)
    pygame.draw.rect(screen, (255, 251, 212), (x_pos,y_pos+110, 100,100))
        # TODO: DRAW THE MOVING OBJECT (e.g., a rectangle or circle)
    pygame.draw.rect(screen, (255, 251, 212), (x_pos,y_pos+220, 100,100))
        # TODO: DRAW THE MOVING OBJECT (e.g., a rectangle or circle)
    pygame.draw.rect(screen, (255, 251, 212), (x_pos,y_pos+330, 100,100))
        # TODO: DRAW THE MOVING OBJECT (e.g., a rectangle or circle)
    pygame.draw.rect(screen, (255, 251, 212), (x_pos,y_pos+50, 100,100))
        # TODO: DRAW THE MOVING OBJECT (e.g., a rectangle or circle)
    pygame.draw.rect(screen, (255, 251, 212), (x_pos,y_pos+25, 100,100))
    
    
    screen.blit(Image,(bob_x,bob_y))
    
    
    
    
    
    
    # Update the display
    pygame.display.flip()

    # Delay to control the frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()