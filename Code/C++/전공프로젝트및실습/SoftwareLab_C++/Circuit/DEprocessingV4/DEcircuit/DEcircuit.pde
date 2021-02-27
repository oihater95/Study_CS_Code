RLC s1,s2,s3;
void setup(){
  size(1000,800);
  stroke(0,0,255);
  s1 = new RLC(48,280,100,0.4);
  frameRate(10);
  background(120);
}
void draw(){  
  if(s1.t<6e-3) s1.update();
}
