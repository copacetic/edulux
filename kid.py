import simulator as sim
import random

sim.init(True, True)

monkey = sim.Group([sim.light_list[3],sim.light_list[1]], True)

print monkey[0].id_code
print monkey[1].id_code

monkey.set_color((255,0,0))

sim.keep_run()
