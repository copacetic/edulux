// C 
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// C++ 
#include <vector>

// ArtNet
#include <artnet/artnet.h>

using std::vector;

#define SUBNET_ADDR 0
#define MAX_CHANNELS 512
// we allow only 0 as the valid subnet (artnet term) value
#define MAX_UNIVERSES 15
#define VERBOSITY 0
#define BCAST_LIMIT 0

typedef unsigned char dmx_t;

struct Universe{
	int universe_id;
	dmx_t * dmx;
	artnet_node node;
}; 

int sanity_check_color(int);

int sanity_check_channel(int);

Universe * get_universe_from_id(int);

void set_lights(artnet_node, dmx_t *);

int clear_lights(int);

int flush(int);

int start_universe(int);

int stop_universe(int);

int add_universe(int);

int close_universe(int);

int set_light(int, int, int, int, int, int, int);
