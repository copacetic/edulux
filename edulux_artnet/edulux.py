from ctypes import *

loaded_universes=[]
active_universe=None
init_called=False
libedulux={}

def load_universe(universe):
	if universe not in loaded_universes:
		add_uni_res = libedulux["add_universe"](universe)
		if add_uni_res != 0:
			print "Edulux: error returned in flush_values:add_universe"
			return 1
		loaded_universes.append(universe)
	return 0

def set_light_value(universe, r_channel, g_channel, b_channel, r, g, b):
	if get_initialized() is False:
		return 1
	if load_universe(universe) != 0:
		return 1

	res = libedulux["set_light"](universe, r_channel, g_channel, b_channel, r, g, b)
	
	if res != 0:
		print "Edulux: error returned in set_light_value:set_light"
		return 1
	return 0

def flush_values(universe):
	global active_universe
	if get_initialized() is False:
		return 1

	if load_universe(universe) != 0:
		return 1

	if active_universe != universe:
		if active_universe != None:
			stop_uni_res = libedulux["stop_universe"](active_universe)
			if stop_uni_res != 0:
				print "Edulux: error returned in flush_values:stop_universe"
				return 1
		start_uni_res = libedulux["start_universe"](universe)
		if start_uni_res != 0:
			print "Edulux: error returned in flush_values:start_universe"
			return 1
		active_universe = universe
	
	flush_res = libedulux["flush"](universe)
	if flush_res != 0:
		print "Edulux: error returned in flush_values:flush"
	return 0

def finish():
	global loaded_universes
	if get_initialized() is False:
		return 1

	if active_universe != None:
		stop_uni_res = libedulux["stop_universe"](active_universe)
		if stop_uni_res != 0:
			print "Edulux: error returned in flush_values:stop_universe"
			return 1

	for universe in loaded_universes:
		res = libedulux["close_universe"](universe)
		if res != 0:
			print "Edulux: error returned in finish:close_universe"
	
	loaded_universes = []

def get_initialized():
	if init_called is False:
		print "Edulux: You cannot run other module functions until you call init!"
		return False
	else:
		return True

def init():
	global init_called
	global libedulux

	# Load the edulux library
	edulux = cdll.LoadLibrary("libedulux.so");

	# Give function pointers more palatable names
	# Node the names are mangled, they were retrieved
	# by using the strings command on the libedulux.so
	start_universe = edulux._Z14start_universei
	stop_universe = edulux._Z13stop_universei
	clear_lights = edulux._Z12clear_lightsi
	add_universe = edulux._Z12add_universei
	close_universe = edulux._Z14close_universei
	flush = edulux._Z5flushi
	set_light = edulux._Z9set_lightiiiiiii

	# Define argument types
	clear_lights.argtypes = [c_int]
	flush.argtypes = [c_int]
	start_universe.argtypes = [c_int]
	stop_universe.argtypes = [c_int]
	add_universe.argtypes = [c_int]
	close_universe.argtypes = [c_int]
	set_light.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int]

	# Define return types
	clear_lights.restype = c_int
	flush.restype = c_int
	start_universe.restype = c_int
	stop_universe.restype = c_int
	add_universe.restype = c_int
	close_universe.restype = c_int
	set_light.restype = c_int

	libedulux["start_universe"] = start_universe
	libedulux["stop_universe"] = stop_universe
	libedulux["add_universe"] = add_universe
	libedulux["close_universe"] = close_universe
	libedulux["flush"] = flush
	libedulux["set_light"] = set_light

	init_called = True
