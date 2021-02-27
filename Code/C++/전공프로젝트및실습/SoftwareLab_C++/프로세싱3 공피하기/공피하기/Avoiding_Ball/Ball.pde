

class Ball
{
  float xLoc;
  float yLoc;
  float vx, vy;
  float hue1, hue2;
  float dim, rad;
  float accel;

  Ball(float x, float y, float d) {

    xLoc = x;
    yLoc = y;
    vx =  3;
    vy =  3;
    dim = d;
    rad = d/2;
    accel = 1.1;
  }

  void move()
  {
    if(vx > 7 && vy > 7)
    {
      accel = 1;
    }
    
    if (xLoc-rad < 0)
    {
      vx = - vx;
      vx *= accel;
    } else if (xLoc + rad > width)
    {
      vx = -vx;
      vx *= accel;
    } else if (yLoc - rad < 0)
    {
      vy = -vy;
      vy *= accel;
    } else if (yLoc + rad > height)
    {
      vy = -vy;
      vy *= accel;
    }
    
 
    xLoc = xLoc + vx;
    yLoc = yLoc + vy;

    hue1 = random(0, 50);
    hue2 = random(100, 200);
  }

  void display()
  {
    stroke(hue1, 255, 0);
    fill(hue1, 255, 255);
    ellipse(xLoc, yLoc, dim, dim);
    fill(hue2, 255, 255);
    ellipse(xLoc, yLoc, dim, rad);
  }

  boolean collide(Pad pp)
 {
    if (this.xLoc-this.rad<pp.xLoc-pp.rad && this.xLoc+this.rad>pp.xLoc+pp.rad && this.yLoc+this.rad>pp.yLoc-pp.rad && this.yLoc-this.rad<pp.yLoc-pp.rad)
    
      return true;
     
    else if (this.xLoc-this.rad<pp.xLoc-pp.rad && this.xLoc+this.rad>pp.xLoc+pp.rad && this.yLoc-this.rad<pp.yLoc+pp.rad && this.yLoc+this.rad>pp.yLoc+pp.rad)
    
      return true;
     
    else if (this.yLoc-this.rad<pp.yLoc-pp.rad && this.yLoc+this.rad>pp.yLoc+pp.rad && this.xLoc+this.rad>pp.xLoc-pp.rad && this.xLoc-this.rad<pp.xLoc-pp.rad)
    
      return true;
    
    else if (this.yLoc-this.rad<pp.yLoc-pp.rad && this.yLoc+this.rad>pp.yLoc+pp.rad && this.xLoc-this.rad<pp.xLoc+pp.rad && this.xLoc+this.rad>pp.xLoc+pp.rad)
    
      return true;
    
    else
    return false;
 }
}
