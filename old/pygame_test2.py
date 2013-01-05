
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

"""
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
"""

def draw_rings(first_radius, ring_radius):
    for ring_numb in reversed(range (1,9)):
        pygame.draw.circle(screen, c_green, center, ring_numb*first_radius+ring_radius)
        pygame.draw.circle(screen, c_black, center, ring_numb*first_radius)


def draw_lights(first_radius, ring_radius):
    ring_one_difference = 102-87
    ring_two_difference = 124-109
    ring_three_difference = 86-71
    ring_four_difference = 70-55
    ring_five_difference = 108-65
    ring_six_difference = 54-1
    ring_seven_difference = 64-1
    ring_eight_difference = 118-53
    ring_array = [ring_one_difference, ring_two_difference, ring_three_difference, ring_four_difference, ring_five_difference, ring_six_difference, ring_seven_difference, ring_eight_difference]

    for ring_number in range (8):
        number_of_lights = ring_array[ring_number] + 1
        for light_number in range (number_of_lights):
            radians = math.radians(360.0*light_number/number_of_lights)
            x = (first_radius + first_radius*ring_number + ring_radius/2)*math.cos(radians) + center[0]
            y = (first_radius + first_radius*ring_number + ring_radius/2)*math.sin(radians) + center[1]
            pygame.draw.circle(screen, c_red, (int(x),int(y)),3)
"""
def draw_diagram():
    draw_lights()
    draw_rings()
"""

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

        """
        pos[0]=200
        pos[1]=200
        pygame.draw.circle(screen, c_green, tuple(pos), 110)
        pygame.draw.circle(screen, c_black, tuple(pos), 90)
        angle = 360/8
        radians = math.radians(angle)
        for circle_number in range (8):
            x = 100*math.cos(radians*circle_number) + 200
            y = 100*math.sin(radians*circle_number) + 200
            pygame.draw.circle(screen, c_red, (int(x),int(y)),10)
        """
        center = (300,300)
        draw_rings(30,10)
        draw_lights(30,10)
        pygame.display.flip()
        
    pygame.quit()
