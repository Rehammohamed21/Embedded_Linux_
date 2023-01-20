#include <iostream>
#include <pigpio.h>
#include "ssd.h"
using namespace std;

int main()
{
   if (gpioInitialise() < 0) return 1;
   SSD myssd;
   myssd.init();
   while(1)
   {
	   
		myssd.display();
   }
   return 0;
}