class Pad
{
  float xLoc;
  float yLoc;
  float hue;
  float dim, rad;
  float grid;
  
  
  Pad(float d) {
    
    xLoc = mouseX;
    yLoc = mouseY;
    hue = 100;
    dim = d;
    rad = d/2;
    grid = 12;
  }

  void move()
  {
    xLoc = mouseX;
    yLoc = mouseY ;
  // if(keyPressed)
 //  {
  //  if(key == 'a') xLoc -= grid; 
  //  if(key == 'd') xLoc += grid;
   //}
  }

  void display()
  {
   stroke(15,255,255);
   strokeWeight(3);
   fill(10,10,10);
   ellipse(xLoc, yLoc, dim ,dim);
  }
}
