import pygame
import sys

pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BOB")

Image = pygame.image.load("Bob.png")


Image = pygame.transform.scale(Image,(500,400))




Image2 = pygame.image.load("BAD.webp")


Image2 = pygame.transform.scale(Image2,(200,200))

Image2 = pygame.transform.rotate(Image2,90)



Image3 = pygame.image.load("WATER.png")


Image3 = pygame.transform.scale(Image3,(200,200))






# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    screen.fill((255,255,255))
    
    screen.blit(Image,(0,0))
    
    screen.blit(Image2,(129,400))
    
    screen.blit(Image3,(400,400))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

