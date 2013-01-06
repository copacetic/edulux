import simulator as sim
import random
import time

sim.init(True, True)

######### Even Group ###########

even_list = []
for i in range(len(sim.light_list)):
	if sim.light_list[i].id_code%2 == 0:
		even_list.append(sim.light_list[i])
even_group = sim.Group(even_list,True)

########## Odd Group ############

odd_list = []
for i in range(len(sim.light_list)):
	if sim.light_list[i].id_code%2 != 0:
		odd_list.append(sim.light_list[i])
odd_group = sim.Group(odd_list,True)

########## All Group ############

all_group = sim.Group(sim.light_list,False)

#################################

########## Ring Group ###########

ring_list = []
ring_numbs = [(0,4),(5,20),(21,36),(37,52),(53,68),(69,112),(113,166),(167,230),(231,296),(297,324),(325,332)]

for i in range(





#################################


for i in range(odd_group.length()):
    #odd_group[i].set_color((0,0,255))
    time.sleep(0.01)

sim.keep_run()
