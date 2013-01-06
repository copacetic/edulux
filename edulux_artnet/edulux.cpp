#include "edulux.h"

Universe* universes[MAX_UNIVERSES];
int univ_size = 0;

int sanity_check_color(int color)
{
	if( color < 0 || color > 255 )
		return 1;
	return 0;
}

int start_universe(int universe)
{
	artnet_node temp;
	Universe * uni = get_universe_from_id(universe);
	if( uni == NULL )
		return 1;
	else
		artnet_start(uni->node);
	return 0;
}

int stop_universe(int universe)
{
	Universe * uni = get_universe_from_id(universe);
	if( uni == NULL )
		return 1;
	else
		artnet_stop(uni->node);
	return 0;
}

int sanity_check_channel(int channel)
{
	if( channel < 0 || channel > MAX_CHANNELS )
		return 1;
	return 0;
}

Universe * get_universe_from_id(int universe)
{
	int i;
	for( i=0; i < univ_size; i++ )
	{
		if( universes[i] != NULL )
		{
			if(universes[i]->universe_id == universe )
				return universes[i];
		}
	}
	return NULL;
}

void set_lights(artnet_node set_me, dmx_t * dmx)
{
	artnet_send_dmx(set_me,0,MAX_CHANNELS,dmx);
}

int clear_lights(int universe)
{
	Universe * uni = get_universe_from_id(universe);
	if( uni != NULL )
	{
		memset(uni->dmx, 0, MAX_CHANNELS*sizeof(dmx_t));
		set_lights(uni->node, uni->dmx);
		return 0;
	}
	return 1;
}

int add_universe(int universe)
{
	char * ip_addr = 0;
	int verbose = 0;
	int bcast_limit = 0;

	// sanity check
	if( universe > MAX_UNIVERSES || universe < 0)
		return 1;

	artnet_node srv;
	srv = artnet_new(ip_addr, verbose);
	
	if( srv == NULL ) return 1;

	artnet_set_short_name(srv, "Simple ArtNet Signaler");
	artnet_set_long_name(srv, "Tumo's Fountain Project Artnet Signaler");
	
	artnet_set_node_type(srv, ARTNET_SRV);
	artnet_set_subnet_addr(srv, SUBNET_ADDR);
	artnet_set_port_type(srv, 0, ARTNET_ENABLE_INPUT, ARTNET_PORT_DMX);
	artnet_set_port_addr(srv, 0, ARTNET_INPUT_PORT, universe);

	artnet_set_bcast_limit(srv, bcast_limit);

	dmx_t * dmx = new dmx_t[MAX_CHANNELS+10];

	Universe * uni = new Universe;
	uni->universe_id = universe;
	uni->dmx = dmx;
	uni->node = srv;
	//add size check here
	universes[univ_size]=uni;
	univ_size++;
	return 0;
}

int close_universe(int universe)
{
	bool found = false;
	int i;
	for( i=0; i < univ_size; i++ )
	{
		if( universes[i] != NULL )
		{
			if( universes[i]->universe_id == universe )
			{
				artnet_destroy(universes[i]->node);
				delete universes[i]->dmx;
				found = true;
				break;
			}
		}
	}
	if( found == true )
	{
		delete universes[i];
		univ_size--;

	}else{
		return 1;
	}
	return 0;
}

int flush(int universe)
{
	Universe* uni = get_universe_from_id(universe);
	if( uni == NULL )
		return 1;
	else
		set_lights(uni->node, uni->dmx);
		return 0;
}

int set_light(int universe, int r_channel, int g_channel, int b_channel, int red, int green, int blue)
{
	// sanity checks on channel values
	if( sanity_check_channel(r_channel)==1 )
		return 1;
	if( sanity_check_channel(g_channel)==1 )
		return 1;
	if( sanity_check_channel(b_channel)==1 )
		return 1;

	// sanity checks on color values
	if( sanity_check_color(red)==1 )
		return 1;
	if( sanity_check_color(green)==1 )
		return 1;
	if( sanity_check_color(blue)==1 )
		return 1;

	Universe * uni = get_universe_from_id(universe);
	if( uni == NULL ) return 1;
	dmx_t * dmx = uni->dmx;
	artnet_node srv = uni->node;

	dmx[r_channel] = red;
	dmx[b_channel] = blue;
	dmx[g_channel] = green;
}
