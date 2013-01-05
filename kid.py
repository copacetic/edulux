import simulator as sim
import random

sim.init()

for i in range (1,50):
    sim.light_list[i].set_color((random.random()*255,0,0))

sim.keep_run()
