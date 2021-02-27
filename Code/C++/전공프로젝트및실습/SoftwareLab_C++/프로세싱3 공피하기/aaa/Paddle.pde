class Pad
{
  float xLoc;
  float yLoc;
  float hue;
  float dim, rad;

  Pad(float d) {
    
    xLoc = mouseX;
    yLoc = mouseY;
    hue = 100;
    dim = d;
    rad = d/2;
    
  }

  void move()
  {
    xLoc = mouseX;
    yLoc = mouseY;
  }

  void display()
  {
   strokeWeight(5);
   fill(50,255,100);
   ellipse(xLoc, yLoc, 30, 30);
  }
}
