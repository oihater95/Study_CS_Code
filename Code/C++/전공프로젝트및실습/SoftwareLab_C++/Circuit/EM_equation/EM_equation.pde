stringWave s1;
void setup(){
  size(1000,800);
  stroke(0,0,255);
  s1 = new stringWave();
 
  frameRate(200);
}
void draw(){  
  background(120);
  s1.update();
  
}
