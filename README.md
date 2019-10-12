## Requirments:

- Python 3
- pySerial

## Commands:

Commands are sent by sending the byte on the Serial then waiting a delay. After the delay the script reads everything in the Serial buffer.

|Byte | Description      |
|:---:|------------------|
|0x00 |Requestions information from connected device|
