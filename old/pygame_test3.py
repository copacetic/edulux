
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

    def set_color(self, color):
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


def draw_rings(ring_thickness, number_of_rings, radius_array):
    for ring_numb in reversed(range (0,number_of_rings)):
        pygame.draw.circle(screen, c_green, center, radius_array[ring_numb]+ring_thickness)
        pygame.draw.circle(screen, c_black, center, radius_array[ring_numb])


def compute_lights(number_of_rings, ring_thickness, light_radius, radius_array):
    ring_zero_difference = 107-103
    ring_one_difference = 102-87
    ring_two_difference = 124-109
    ring_three_difference = 86-71
    ring_four_difference = 70-55
    ring_five_difference = 108-65
    ring_six_difference = 54-1
    ring_seven_difference = 64-1
    ring_eight_difference = 118-53
    ring_array = [ring_zero_difference, ring_one_difference, ring_two_difference, ring_three_difference, ring_four_difference, ring_five_difference, ring_six_difference, ring_seven_difference, ring_eight_difference]
    light_id = 1
    lights_list = []
    for ring_number in range (number_of_rings):
        number_of_lights = ring_array[ring_number] + 1
        for light_number in range (number_of_lights):
            radians = math.radians(360.0*light_number/number_of_lights)
            x = (ring_thickness/2 + radius_array[ring_number])*math.cos(radians) + center[0]
            y = (ring_thickness/2 + radius_array[ring_number])*math.sin(radians) + center[1]
            lights_list.append(Light(c_red, (int(x),int(y)), light_radius, light_id))
            light_id += 1
    return lights_list

def draw_lights(lights_list):
    for i in range (len(lights_list)):
        light = lights_list[i]
        light.draw()

    

def draw_diagram(first_radius, ring_thickness, number_of_rings, light_radius, radius_array):
    for i in range(1,number_of_rings):
        radius_array[i] += radius_array[i-1] 
    draw_rings(ring_thickness, number_of_rings, radius_array)
    draw_lights(compute_lights(number_of_rings, ring_thickness, light_radius, radius_array))

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

        radius_array = [30,40,30,30,30,40,50,50]
        center = (300,300)
        draw_diagram(30,10,8,5,radius_array)
        pygame.display.flip()
        
    pygame.quit()
