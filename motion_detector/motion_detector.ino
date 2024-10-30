int buzzer = 2;
int PIR_sensor = 3;

void setup()
{
  pinMode(buzzer, OUTPUT);
  pinMode(PIR_sensor, INPUT);
  Serial.begin(9600);
  }

void loop()
{
  int sensor_state = digitalRead(PIR_sensor);
  
  if (sensor_state == 1) {
    digitalWrite(buzzer, HIGH);
  } else {
    digitalWrite(buzzer, LOW);
  }
  Serial.println(sensor_state);
 }
