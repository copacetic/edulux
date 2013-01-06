import edulux

edulux.init()
edulux.set_light_value(1, 0, 1, 2, 255, 0, 0)
edulux.set_light_value(2, 0, 1, 2, 255, 0, 0)
edulux.set_light_value(3, 0, 1, 2, 255, 0, 0)

edulux.flush_values(1)
edulux.flush_values(2)
edulux.flush_values(3)

edulux.finish()
