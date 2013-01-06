#include <unistd.h>
#include "edulux.h"

void set_all_in_universe(int universe, int r, int g, int b)
{
	for(int i=0; i < 512 - 2; i+=3)
	{
		set_light(universe, i, i+1, i+2, r, g, b);
	}
}

void set_range_in_universe(int universe, int start_channel, int end_channel, int r, int g, int b)
{
	for(int i=start_channel; i < end_channel - 2; i+=3)
	{
		set_light(universe, i, i+1, i+2, r, g, b);
	}

}
int main()
{
	int uni_code = 0;
	int start_c = 0;
	int end_c = 0;
	
	for(int universe=1; universe < 4; universe++)
		add_universe(universe);

	for(int universe=1; universe < 4; universe++)
	{
		start_universe(universe);
		clear_lights(uni_code);
		switch(universe)
		{
		case 1:
			set_all_in_universe(universe, 255, 0, 0);
			break;	
		case 2:
			set_all_in_universe(universe, 0, 255, 0);
			break;
		case 3:
			set_all_in_universe(universe, 0, 0, 255);
			break;
		}
		flush(universe);
		stop_universe(universe);
		sleep(1);
	}
	sleep(1);
	for(int universe=1; universe < 4; universe++)
	{
		start_universe(universe);
		clear_lights(universe);
		stop_universe(universe);
	}
	sleep(2);
	for(int universe=1; universe < 4; universe++)
		close_universe(universe);
	return 0;
}
