Ball b1, b2, b3;
Pad p;
void setup() {
  size(800, 600);
  print(width, height);
  colorMode(HSB);
  b1 = new Ball(100, 100, 50);
   b2 = new Ball(200 , 400, 100);
  b3 = new Ball(400, 250, 150);
  p = new Pad(200);
  strokeWeight(5);
}

void draw() {
  background(250);
  b1.move();
  b1.display();
   b2.move();
  b2.display();
  b3.move();
  b3.display();
  p.move();
  p.display();
 
}
