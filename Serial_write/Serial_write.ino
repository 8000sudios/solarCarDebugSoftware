byte msg[2] = {0x32, 0xFF};
byte rByte;


void setup() {
  Serial.begin(9600);

  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}

void loop() {
  
  while (Serial.available() == 0) {}
  digitalWrite(13, LOW);
  rByte = Serial.read();
  Serial.write(msg, 2);
   
}
