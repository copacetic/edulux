import simulator as sim
import random
import time

sim.init(True, True)

########## All Group ############
all_group = sim.Group(False, sim.light_list)

######### Even Group ###########
even_list = []
for i in range(len(sim.light_list)):
	if sim.light_list[i].id_code%2 == 0:
		even_list.append(sim.light_list[i])
even_group = sim.Group(True, even_list)

########## Odd Group ############
odd_list = []
for i in range(len(sim.light_list)):
	if sim.light_list[i].id_code%2 != 0:
		odd_list.append(sim.light_list[i])
odd_group = sim.Group(True, odd_list)

########## Ring Group ###########
ring_list = []
ring_numbs = [(0,4),(5,20),(21,36),(37,52),(53,68),(69,112),(113,166),(167,230),(231,296),(297,324),(325,332)]
for r in range(len(ring_numbs)):
    ring_list.append(sim.Group(False, []))
    for i in range(ring_numbs[r][0],ring_numbs[r][1] +1):
        ring_list[r].append(sim.light_list[i])
ring_group = sim.Group(False, ring_list)

########## Quad Group ###########
quad1_list = [332,331,324,323,322,321,320,319,318,236,235,234,233,232,231,296,295,294,293,292,291,290,289,288,287,286,172,171,170,169,168,167,230,229,228,227,226,225,224,223,222,221,220,117,116,115,114,113,166,165,164,163,162,161,160,159,158,72,71,70,69,112,111,110,109,108,107,106,53,52,21,20,68,51,36,19,4,67,50,35,18,66,49,34,17]
quad2_list = [205,270,329,330, 311, 312, 313, 314, 315, 316, 317, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 63,64,65,46,47,48,31,32,33,16,15,14,3]
quad3_list = [327,328,304, 305, 306, 307, 308, 309, 310, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 58,59,60,61,62,41,42,43,44,45,26,27,28,29,30,9,10,11,12,13,1,2]
quad4_list = [325,326, 297, 298, 299, 300, 301, 302, 303, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 54,55,56,57,37,38,39,40,22,23,24,25,5,6,7,8,0]

quads_list = [quad1_list, quad2_list, quad3_list, quad4_list]
quadgroup_list = []
for quadnumber in range(len(quads_list)):
    quadgroup_list.append(sim.Group(False, []))
    for l in quads_list[quadnumber]:
        quadgroup_list[quadnumber].append(sim.light_list[l])

quad_group = sim.Group(False, quadgroup_list)
 
########## H Half Group ###########
h_half_group = sim.Group.groupify(sim.Group.groupify(quad_group[0],quad_group[1]), sim.Group.groupify(quad_group[2], quad_group[3]))

########## V Half Group ###########
v_half_group = sim.Group.groupify(sim.Group.groupify(quad_group[0],quad_group[3]), sim.Group.groupify(quad_group[1], quad_group[2]))

#######################################################:

#v_half_group[1].set_color((255,0,0))
#sim.flush_pygame()

for i in range(50):
	for i in range(4):
	    quad_group[i].set_color((random.randrange(2)*255,random.randrange(2)*255,random.randrange(2)*255))
	    sim.flush_pygame()
	    time.sleep(0.5)

'''
for i in range(new_group.length()):
	new_group[i].set_color((255,0,0))
	sim.flush_pygame()
	time.sleep(0.1)
'''
