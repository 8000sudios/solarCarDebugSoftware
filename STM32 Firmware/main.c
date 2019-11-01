#include "stm32f10x.h"
#include "CAN.h"
#include "virtual_com.h"

int main(void) {
	CANInit(CAN_500KBPS);
	VirtualComInit();
	
	CAN_msg_t CAN_rx_msg;
	CAN_msg_t CAN_tx_msg;
	
	while(1) {
	
		while(!CANMsgAvail()) {
		}
			
		CANReceive(&CAN_rx_msg);
		
		SendString("ID: ");
		SendInt(CAN_rx_msg.id);
		SendString(" Message: ");
		for(int i = 0; i < 8; i++) {
			SendInt8(CAN_rx_msg.data[i]);
			SendString(" ");
		}
		SendLine();
	}
	
}