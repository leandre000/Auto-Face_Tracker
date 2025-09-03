// Auto Face Tracker
const int STEP_PIN=2, DIR_PIN=3, EN_PIN=4;
void setup(){
  Serial.begin(115200);
  pinMode(STEP_PIN,OUTPUT);pinMode(DIR_PIN,OUTPUT);pinMode(EN_PIN,OUTPUT);
  digitalWrite(EN_PIN,LOW);
  Serial.println("READY");
}
void loop(){
  if(Serial.available()){
    String cmd=Serial.readStringUntil('\n');
    char dir=cmd.charAt(0);
    int steps=cmd.substring(1).toInt();
    if(dir=='L'||dir=='R'){
      digitalWrite(DIR_PIN,dir=='R');
      for(int i=0;i<steps;i++){
        digitalWrite(STEP_PIN,HIGH);delayMicroseconds(1000);
        digitalWrite(STEP_PIN,LOW);delayMicroseconds(1000);
      }
      Serial.println("OK");
    }
  }
}
