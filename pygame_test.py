
import sys, pygame, random, math
random.seed()
pygame.init()
pygame.font.init()
from pygame.locals import *

now = pygame.time.get_ticks()

size = width,height = 800,600

c_green = 0,255,0
c_red = 255,0,0
c_blue = 0,0,255
c_white = 255,255,255
c_black = 0,0,0

class Light:
    def __init__(self, color, pos, radius, id_code):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.id_code = id_code

    def set_color(color):
        self.color = color

    def draw():
        pygame.draw.circ
def compute_rings():

def compute_lights():

def draw_rings():

def draw_lights():

def draw_diagram():
    draw_lights()
    draw_rings()

if __name__ == "__main__":
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Fountain Simulation")

   
    cont = True
    pos=[100,100]
    while cont:
        start_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: cont = False;
        screen.fill(c_black)

        pos[0]=200
        pos[1]=200
        pygame.draw.circle(screen, c_green, tuple(pos), 100)
        angle = 360/8
        radians = math.radians(angle)
        for circle_number in range (8):
            x = 100*math.cos(radians*circle_number) + 200
            y = 100*math.sin(radians*circle_number) + 200
            pygame.draw.circle(screen, c_red, (int(x),int(y)),10)

        pygame.display.flip()
        
    pygame.quit()
