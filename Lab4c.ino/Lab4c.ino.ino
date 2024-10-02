int ledPin = 13; // Pin for the built-in LED on Arduino

void setup() {
  pinMode(ledPin, OUTPUT); // Set the LED pin as output.
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) { // Check if there's incoming data
    char command = Serial.read(); // Read the incoming byte
    if (command == '1') {
      digitalWrite(ledPin, HIGH); // Turn the LED on
    } 
    else if (command == '0') {
      digitalWrite(ledPin, LOW); // Turn the LED off
    }
  }
}