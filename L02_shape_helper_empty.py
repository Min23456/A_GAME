import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1500, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Drawer")

white = (255, 255, 255)

black = (0, 0, 0)

light_blue = (215, 236, 250)

organic_green = (126, 173, 110)

organic_orange = (255, 165, 0)

organic_black = (27,22,27)

# Function to draw a rectangle
def draw_rectangle(surface, color,x,y,width, height):
    pygame.draw.rect(surface, color, (x, y, width, height))

# Function to draw a circle
def draw_circle(surface, color,x, y, radius):
    pygame.draw.circle(surface, color, (x, y), radius)

# Function to draw a triangle
def draw_triangle(surface, color, point1, point2, point3):
    pygame.draw.polygon(surface, color, [point1, point2, point3])

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)

    
  
    draw_circle(screen,organic_green,100,100,400)
    
    
    draw_rectangle(screen,organic_black,350,200,500,500)
    
    
    draw_triangle(screen,light_blue,(600,400),(200,900),(1000,1000))
    
    
    draw_rectangle(screen,black,0,0,300,300)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

