int LED = 3;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(LED, 0);//Turns off the LED
  delay(500);
  analogWrite(LED, 50);
  delay(500);
  analogWrite(LED, 100);
  delay(500);
  analogWrite(LED, 150);
  delay(500);
  analogWrite(LED, 200);
  delay(500);
  analogWrite(LED, 250);
  delay(500);
  analogWrite(LED, 255);//Makes the LED fully bright
  delay(500);
}
