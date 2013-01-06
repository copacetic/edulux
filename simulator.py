
import sys, pygame, random, math
random.seed()
pygame.init()
pygame.font.init()
from pygame.locals import *

c_green = 0,255,0
c_red = 255,0,0
c_blue = 0,0,255
c_white = 255,255,255
c_black = 0,0,0
c_darkgrey = 20,20,20
c_lightgrey = 150,150,150

pos=[100,100]
radius_array = [30,40,30,30,30,40,50,50,40,40,40]
size = width,height = 950,950
center = width/2,height/2
pygame.display.set_caption("Fountain Simulation")
screen = pygame.display.set_mode(size)
screen.fill(c_black)
font = pygame.font.SysFont("Arial", 10)
    
showRings = False
showNumb = False

light_list = []

class Group:
    def __init__(self, contents, sort):
        self.contents = contents
        self.sort = sort
        if sort:
            self.contents = sorted(contents)

    def __getitem__(self, index):
        return self.contents[index]

    def append(self, item):
	self.contents.append(item)
    
    def set_color(self, color):
        for light in self.contents:
            light.set_color(color)
    def length(self):
        return len(self.contents)
  
class Light:
    def __init__(self, pos, radius, id_code, universe, real_id, color = c_lightgrey):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.id_code = id_code
        self.universe = universe
        self.real_id = real_id

    def __cmp__(self, other):
        if self.id_code > other.id_code: return 1
        else: return -1

    def set_color(self, color):
        self.color = color
        self.draw()
        pygame.display.flip()
        #hayg.set_light(self.universe,(self.real_id*(3-2)),(self.real_id(3-1)),(self.real_id(3-0)),color[0],color[1],color[2])  
    def off():
        self.set_color(c_lightgrey)

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        
        if showNumb:
            local_label = font.render(str(self.id_code), 1, c_white)
            screen.blit(local_label, (self.pos[0],self.pos[1]))

        #real_label = font.render(str(self.real_id), 1, c_white)
        #screen.blit(real_label, (self.pos[0]-10,self.pos[1]-10))

def draw_rings(ring_thickness, number_of_rings, radius_array):
    for ring_numb in reversed(range (0,number_of_rings)):
        pygame.draw.circle(screen, c_darkgrey, center, radius_array[ring_numb]+ring_thickness)
        pygame.draw.circle(screen, c_black, center, radius_array[ring_numb])


def compute_lights(number_of_rings, ring_thickness, light_radius, radius_array):
    global light_list

    ring_zero_difference = (107-103, 162 ,3)
    ring_one_difference = (102-87, 175.5 ,3)
    ring_two_difference = (124-109, 198, 2)
    ring_three_difference = (86-71, 175.5, 3)
    ring_four_difference = (70-55, 198, 3)
    ring_five_difference = (108-65, 210.7, 2)
    ring_six_difference = (54-1, 210, 3)
    ring_seven_difference = (64-1, 209, 2)
    ring_eight_difference = (118-53, 209, 1)
    ring_nine_difference = (52-25, 145.6, 1, 60.0, 12/4, 7)
    ring_ten_difference = (24-17, 137.72, 1, 84.48, 65.45/4, 2) 
    ring_array = [ring_zero_difference, ring_one_difference, ring_two_difference, ring_three_difference, ring_four_difference, ring_five_difference, ring_six_difference, ring_seven_difference, ring_eight_difference, ring_nine_difference, ring_ten_difference]
    light_id = 0
    count3 = 107
    count2 = 124
    count1 = 118

    for ring_number in range(number_of_rings):
        number_of_lights = ring_array[ring_number][0]+ 1
        acc_angle = 0
        for light_number in range (number_of_lights):
            if ring_number > 8:
                radians = -math.radians(360.0*light_number/(ring_array[ring_number][0]*ring_array[ring_number][4])) + math.radians(ring_array[ring_number][1])
                if light_number%ring_array[ring_number][5] == 0 and light_number != 0:
                    acc_angle += math.radians(ring_array[ring_number][3] - (360.0/(ring_array[ring_number][0]*ring_array[ring_number][4])))
                x = (ring_thickness/2 + radius_array[ring_number])*math.cos(radians-acc_angle) + center[0]
                y = (ring_thickness/2 + radius_array[ring_number])*math.sin(radians-acc_angle) + center[1]
            else:
                radians = -math.radians(360.0*light_number/number_of_lights) + math.radians(ring_array[ring_number][1])
                x = (ring_thickness/2 + radius_array[ring_number])*math.cos(radians) + center[0]
                y = (ring_thickness/2 + radius_array[ring_number])*math.sin(radians) + center[1]
            uni_number = ring_array[ring_number][2]
            if uni_number == 3:
                light_list.append(Light((int(x),int(y)), light_radius, light_id, uni_number, count3))
                count3 -= 1
            elif uni_number == 2:
                light_list.append(Light((int(x),int(y)), light_radius, light_id, uni_number, count2))
                count2 -= 1
            else:
                light_list.append(Light((int(x),int(y)), light_radius, light_id, uni_number, count1))
                count1 -= 1

            light_id += 1

def draw_lights():
    for i in range (len(light_list)):
        light = light_list[i]
        light.draw()

def draw_diagram(ring_thickness, number_of_rings, light_radius, radius_array):
    for i in range(1,number_of_rings):
        radius_array[i] += radius_array[i-1] 
    if showRings:
        draw_rings(ring_thickness, number_of_rings, radius_array)

    compute_lights(number_of_rings, ring_thickness, light_radius, radius_array)
    draw_lights()

"""
def flush()
    for i in range(1,4)
        hayg.flush(i)
"""
     
def init(should_show_ring, should_show_numb):
    global showRings, showNumb

    if should_show_ring:
        showRings = True
    if should_show_numb:
        showNumb = True
    draw_diagram(10,len(radius_array),8,radius_array)
    pygame.display.flip()

def keep_run():
    cont = True
    while cont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: cont = False;
    pygame.quit()

