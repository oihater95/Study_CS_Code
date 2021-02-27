Ball b, b1, b2, b3, b4;
Pad p;
int score = 0;
boolean playOn, playOn1, playOn2, playOn3, playOn4;

void setup() {
  size(800, 600);
  print(width, height);
  colorMode(HSB);
  b = new Ball(100, 100, 50);
  b1 = new Ball(100, 100, 60);
  b2 = new Ball(100, 100, 70);
  b3 = new Ball(100, 100, 80);
  b4 = new Ball(100, 100, 90);

  p = new Pad(15);

  strokeWeight(5);
}

void draw() {
  background(200);

  playOn = b.collide(p);
  playOn1 = b1.collide(p);
  playOn2 = b2.collide(p);
  playOn3 = b3.collide(p);
  playOn4 = b4.collide(p);




  if (playOn == true || playOn1 == true || playOn2 == true || playOn3 == true || playOn4 == true)
  {
    textSize(32);
    fill(10, 200, 200);
    text("Game Over!", width/2, height/2);
    if (score == 0)
    {
      score = frameCount;
    }
    text(score, width/2, height/2+100);
  } else
  {

    if (frameCount <= 400)
    {
      b.move();
      b.display();
    } else if (frameCount>400 && frameCount<=700 )
    {
       b.move();
      b.display();
      b1.move();
      b1.display();
    } else if (frameCount >700 && frameCount <=1100)
    {
      b.move();
      b.display();
      b1.move();
      b1.display();
      b2.move();
      b2.display();
    } else if (frameCount >1100 && frameCount<=1500)
    {
      b.move();
      b.display();
      b1.move();
      b1.display();
      b2.move();
      b2.display();
      b3.move();
      b3.display();
    } else if (frameCount >1500)
    {
     b.move();
      b.display();
      b1.move();
      b1.display();
      b2.move();
      b2.display();
      b3.move();
      b3.display();
      b4.move();
      b4.display();
    }


    p.move();
    p.display();
  }
}
