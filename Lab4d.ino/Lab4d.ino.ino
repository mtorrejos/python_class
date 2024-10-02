int pushButton = 10; //Pin for the push button input

void setup() {
  pinMode(pushButton, INPUT);
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  int buttonValue = digitalRead(pushButton);

  if (buttonState == HIGH) {
    Serial.println("on");  // Send "on" when button is pressed
  } else {
    Serial.println("off"); // Send "off" when button is released
  }
  delay(500);  // Short delay to prevent spamming the serial output
  
}