import simulator as sim
import random

sim.init()

for i in range (0,214):
    sim.light_list[i].set_color((255,0,0))

sim.keep_run()
