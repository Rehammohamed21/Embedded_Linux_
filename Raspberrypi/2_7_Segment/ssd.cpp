#include <pigpio.h>
#include <unistd.h>
#include "ssd.h"


SSD::SSD()
{
	
}
void SSD::init()
{
    int i;
    for(i=0;i<7;i++)
    {
        gpioSetMode(SSD_PORT1[i],PI_OUTPUT);
        gpioSetMode(SSD_PORT2[i],PI_OUTPUT);
    }
}

void SSD::display()
{
    int i,j;
	int k = 0;
	#display 2 7-segment
	for (k=0; k<10; k++)
	{
		for(i=0;i<10;i++)
    {
        for(j=0;j<7;j++)
        {
            gpioWrite(SSD_PORT2[j],((num_display[k]>>j)&1));
			gpioWrite(SSD_PORT1[j],((num_display[i]>>j)&1));
        }
        usleep(500000);
       
    }
	}
    

}