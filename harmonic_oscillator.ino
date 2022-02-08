
void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(2);
}

int d = 1000;
void loop() {
  if (Serial.available()){
    int new_d = Serial.parseInt()/2;
    if (new_d>=10 and new_d<10000){
      d = new_d;
    }
    Serial.print("delay:");
    Serial.println(d);
  }
  //Serial.println("beep");
  digitalWrite(4, HIGH);
  delay(d);           
  digitalWrite(4, LOW); 
  delay(d);  
}
