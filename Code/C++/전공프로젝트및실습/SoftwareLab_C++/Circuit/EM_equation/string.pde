class stringWave {
  stringWave() {
  };
  stringWave(float f)
  {
    c = 3e8;        // wave coefficient
    w = 2.*PI*f;    // display level
    k = w/c;
    dt = 1./f/30;
    dr = c/f/30;
    tpoints = 200;
    Io = 40;
    rlimit = dr*tpoints;
    t = 0;
   }
  int tpoints ; /* total points along string */
  float R0, R1, R2;   /* values at time t */
  float c, w, k, r, Io, t;
  float dr, dt, rlimit;

  void update()
  {
     // boundary condition
     R0 = Io*sin(w*t);
     R1 = R0 - Io*cos(w*t)/PI;
    
    for (int j = 1; j <= tpoints; j++) {                     // location x
      /* boundary condition */
      if ((j == 1) || (j == tpoints))     fxnp1[j] = 0.0;
      // wave equation: d^2 f(x,t) / dt^2 = gamma (d^2 f(x,t) / dx^2 )
      else    fxnp1[j] = 2.0 * fxn[j] - fxnm1[j]
        + sqtau * (fxn[j - 1] - (2.0 * fxn[j]) + fxn[j + 1]);
    }
    /* Update old values with new values */
    for (int j = 1; j <= tpoints; j++) {
      fxnm1[j] = fxn[j];  // f(x, t-dt) = f(x, t)
      fxn[j] = fxnp1[j];  // f(x, t) = f(x, t+dt)
    }
    // draw the result
    stroke(255); 
    line(0, hh, width, hh);
    stroke(0, 0, 255);
    for (int j = 2; j <= tpoints; j++) line(j-1, hh+fxn[j-1]*80, j, hh+fxn[j]*80);
  }
}
