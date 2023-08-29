void DIO_SetPinValue(u8 Port ,u8 Pin , u8 value);
void DIO_SetPinDirection(u8 Port, u8 Pin, u8 Direct);
void DIO_SetPortValue(u8 Port, u8 value);
void DIO_TogglePinValue(u8 Port ,u8 Pin);
u8 DIO_GetPinValue(u8 Port,u8 Pin);
u8 DIO_GetPortValue(u8 Port);

void DIO_SetPortDirection(u8 Direct , u8 value);