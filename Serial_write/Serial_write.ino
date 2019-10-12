void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.write("Things happened! \n");
  delay(1000);
}
