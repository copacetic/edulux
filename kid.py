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
#################################

new_group = sim.Group.merge(False, odd_group, even_group)
print new_group

for i in range(new_group.length()):
	new_group[i].set_color((255,0,0))
	sim.flush_pygame()
	time.sleep(0.1)
