#include "stm32f10x.h"
#include "CAN.h"
#include "virtual_com.h"

int main(void) {
	CANInit(CAN_500KBPS);
	VirtualComInit();
	
	CAN_msg_t CAN_rx_msg;
	CAN_msg_t CAN_tx_msg;
	
	uint8_t time[2];
	
	time[0] = 0xFFUL & (RTC->CNTH);
	time[1] = 0xFFUL & (RTC->CNTL);


	while(1) {
	
		while(!CANMsgAvail()) {
		}
			
		CANReceive(&CAN_rx_msg);

		uint8_t ID_H = 0xFFUL & ( CAN_rx_msg.id >> 8);
		uint8_t ID_L = 0xFFUL & ( CAN_rx_msg.id);

		SendInt8(time[0]);
		SendInt8(time[1]);

		SendInt8(ID_H);
		SendInt8(ID_L);

		for(int i = 0; i < 8; i++) {
			SendInt8(CAN_rx_msg.data[i]);
		}

		SendChar(CAN_rx_msg.len);

		SendLine();
	}
	
}