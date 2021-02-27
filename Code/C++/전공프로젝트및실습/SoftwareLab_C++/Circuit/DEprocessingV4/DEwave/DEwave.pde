stringWave s1,s2,s3;
void setup(){
  size(1000,800);
  stroke(0,0,255);
  s1 = new stringWave(1,height/4);
  s2 = new stringWave(2,height/2);
  s3 = new stringWave(3,height/4*3.0);
  frameRate(200);
}
void draw(){  
  background(120);
  s1.update();
  s2.update();
  s3.update();
}
