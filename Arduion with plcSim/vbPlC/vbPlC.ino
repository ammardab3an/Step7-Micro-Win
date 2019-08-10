int input;
const int Q0_0 = 10;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(2000000);
  pinMode(Q0_0, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    input = Serial.read() - 48;
    if (input == 1) {
      digitalWrite(Q0_0, HIGH);
    }
    if (input == 0) {
      digitalWrite(Q0_0, LOW);
    }
    Serial.println("Done");
    Serial.println(input);
  }
}
