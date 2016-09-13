
int CM11 = 27;
int CM12 = 33;
int HS11 = 29;
int HS12 = 31;
int MS11 = 23;
int MS12 = 25;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(CM11, OUTPUT);  
  pinMode(CM12, OUTPUT);
  pinMode(MS11, OUTPUT);
  pinMode(MS12, OUTPUT);
  pinMode(HS11, OUTPUT);
  pinMode(HS12, OUTPUT); 

}

int Byte1;

void loop() { 
Byte1=Serial.read();
switch (Byte1) {

    case 'A':    
      digitalWrite(CM12, HIGH);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(CM11, LOW);    // turn the LED off by making the voltage LOW
      delay(600);               // wait for a second
      digitalWrite(CM12, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(CM11, LOW);
      break;
    case 'B': 
      digitalWrite(CM12, HIGH);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(CM11, LOW);    // turn the LED off by making the voltage LOW
      delay(750);               // wait for a second
      digitalWrite(CM12, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(CM11, LOW); 
      delay(500); 
      digitalWrite(MS11, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(MS12, HIGH);    // turn the LED off by making the voltage LOW
      delay(500);               // wait for a second
      digitalWrite(MS11, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(MS12, LOW);
      delay(500); 
      digitalWrite(MS12, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(MS11, HIGH);    // turn the LED off by making the voltage LOW
      delay(500);               // wait for a second
      digitalWrite(MS11, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(MS12, LOW);
      break;
    case 'C':
      digitalWrite(CM12, HIGH);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(CM11, LOW);    // turn the LED off by making the voltage LOW
      delay(2200);               // wait for a second
      digitalWrite(CM12, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(CM11, LOW); 
      delay(500); 
      digitalWrite(HS11, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(HS12, HIGH);    // turn the LED off by making the voltage LOW
      delay(500);               // wait for a second
      digitalWrite(HS11, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(HS12, LOW);
      delay(500); 
      digitalWrite(HS12, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(HS11, HIGH);    // turn the LED off by making the voltage LOW
      delay(500);               // wait for a second
      digitalWrite(HS11, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(HS12, LOW);
      break; 
    case 'D':    
      digitalWrite(CM12, HIGH);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(CM11, LOW);    // turn the LED off by making the voltage LOW
      delay(3500);               // wait for a second
      digitalWrite(CM12, LOW);   // turn the LED on (HIGH is the voltage level)              // wait for a second
      digitalWrite(CM11, LOW);
      break;
      
    default:
      break;
  }
}










