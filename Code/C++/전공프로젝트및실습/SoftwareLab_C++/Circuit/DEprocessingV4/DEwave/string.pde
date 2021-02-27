class stringWave {
  stringWave() {
    c = 1.0;
    hh = height/2;
    init_param();
    init_line();
  };
  stringWave(float cc, float hhh) {
    c = cc;        // wave coefficient
    init_param();
    init_line();
    hh = hhh;      // display level
  }

  int tpoints = 1000; /* total points along string */
  float fxn[], fxnp1[], fxnm1[];   /* values at time t */
  float c, sqtau, hh;

  void init_param()
  {
    fxn    = new float[tpoints+2];
    fxnp1  = new float[tpoints+2];
    fxnm1  = new float[tpoints+2];

    float dtime, dx, tau;
    dtime = 0.3;
    dx = 1.0;
    tau = (c * dtime / dx);
    sqtau = tau * tau;
  }
  /***************************************************************************
   *     Initial condition : initial values based on sine curve
   **************************************************************************/
  void init_line()
  {
    float omegax= 6.0 * PI;
    // sine function
    for (int j = 1; j <= tpoints; j++) {
      fxn[j] = sin(omegax * j / tpoints);     // initial condition f(x, t)
      fxnm1[j] = fxn[j];         // initial condition f(x, t-dt) = f(x, t)
    }
    /*/ triangle
    for (int j = 1; j <= tpoints; j++) {
      if(j<tpoints/2) fxn[j] =  (float)j / tpoints*2.0;     // initial condition f(x, t)
      else fxn[j] =  (tpoints-j) / (float)tpoints*2.0;     // initial condition f(x, t)
      fxnm1[j] = fxn[j];         // initial condition f(x, t-dt) = f(x, t)
    }*/
  }
  /***************************************************************************
   *     Update all values along line a specified number of times
   *
   *     Calculate new values using wave equation
   *     d^2 f(x,t) / dt^2 = gamma (d^2 f(x,t) / dx^2 )
   **************************************************************************/
  void update()
  {
    /* Update points along line for this time step */
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
