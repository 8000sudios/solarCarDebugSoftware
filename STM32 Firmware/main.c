#include "stm32f10x.h"
#include "CAN.h"
#include "virtual_com.h"


int main(void) {
	CANInit(CAN_500KBPS);
	VirtualComInit();
	
	int n = 0;
	
	while(!serAvailable()) {
		n++;
	}
	
	n = -1;
	
	SendString("a");
}