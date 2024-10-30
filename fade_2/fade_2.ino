int LED = 3;
int DELAY_MS = 5;//delay between each fade value


void setup() {
  // set the LED pin to an output
  pinMode(LED, OUTPUT);
}

void loop() {
  // fade on
  for(int i = 0; i <= 255; i++){//Loops from 0 to 255
    analogWrite(LED, i);
    delay(DELAY_MS);
  }
  
//fade off
for (int i = 255; i >= 0; i--){//Loops from 255 to 0
   analogWrite(LED, i);
   delay(DELAY_MS);
}
}
