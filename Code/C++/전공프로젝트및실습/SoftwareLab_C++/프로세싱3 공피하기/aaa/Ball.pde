class Ball
{
  float xLoc;
  float yLoc;
  float vx, vy;
  float hue1, hue2;
  float dim, rad;

  Ball(float x, float y, float d) {
    
    xLoc = x;
    yLoc = y;
    vx =  3;
    vy =  3;
    dim = d;
    rad = d/2;
    
  }

  void move()
  {
    xLoc = xLoc + vx;
    yLoc = yLoc + vy;
    if (xLoc-rad < 0)
    {
      vx = - vx;
    } else if (xLoc + rad > width)
    {
      vx = -vx;
    } else if (yLoc - rad < 0)
    {
      vy = -vy;
    } else if (yLoc + rad > height)
    {
      vy = -vy;
    }

    hue1 = random(0, 50);
    hue2 = random(100, 200);
  }

  void display()
  {
    stroke(hue1,255,0);
    fill(hue1, 255, 255);
    ellipse(xLoc, yLoc, dim, dim);
    fill(hue2, 255, 255);
    ellipse(xLoc, yLoc, dim, rad);
  }
    
  }
