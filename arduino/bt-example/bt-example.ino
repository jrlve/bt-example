#include <SoftwareSerial.h>

const int txPin = 9;
const int rxPin = 10;

SoftwareSerial BTSerial(rxPin, txPin); // RX, TX

void setup() {
  BTSerial.flush();
  Serial.begin(9600);
  Serial.println("Enter Messages:");
  BTSerial.begin(9600);
}

void loop() {
  if (BTSerial.available())
    Serial.write(BTSerial.read());
  if (Serial.available())
    BTSerial.write(Serial.read());
}
