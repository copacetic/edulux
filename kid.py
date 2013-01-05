import simulator as sim
import random
import time

sim.init(False, False)

allgroup = sim.Group(sim.light_list,False)

for i in range(allgroup.length()):
    allgroup[i].set_color((0,0,255))
    time.sleep(0.01)

sim.keep_run()
