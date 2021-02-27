Txyt s1;
void setup(){
  size(800,800);
  stroke(0,0,255);
 
  s1 = new Txyt(0.3,0.1);
  //frameRate(30);
  colorMode(HSB);
}
void draw(){  
  background(120);
  s1.update();
}
