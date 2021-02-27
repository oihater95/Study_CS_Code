/****************************************************************************
 * FILE: ser_heat2D.c
 * DESCRIPTION:
 *   Serial HEAT2D Example - C Version
 *   This example is based on a simplified
 *   two-dimensional heat equation domain decomposition.  The initial
 *   temperature is computed to be high in the middle of the domain and
 *   zero at the boundaries.  The boundaries are held at zero throughout
 *   the simulation.  During the time-stepping, an array containing two
 *   domains is used; these domains alternate between old data and new data.
 * AUTHOR: D. Turner
 * Last Revised: 04/15/05 Blaise Barney
 * Last Revised: 03/25/19 Doug Suh           iostream, C++
 * Last Revised: 11/10/19 Doug Suh           Processing3.0 animation
 ****************************************************************************/
class Txyt {
  Txyt() {
    cx = 0.1;
    cy = 0.1;
    inidat();
  }
  Txyt(float cxx, float cyy) {
    cx = cxx;
    cy = cyy;
    inidat();
  }

  int nx = 100;
  int ny = 100;
  float cx,cy;
  float sx,sy; // spacing
  int nn = 0;

  float u0[], u1[];
  /*****************************************************************************
   *  subroutine inidat  ????   f(x, y) = x*(Y-x)*y*(Y-y)    ????
   *****************************************************************************/
  void inidat() {
    int ix, iy;
    u0 = new float[nx*ny];    
    u1 = new float[nx*ny];
    // initial condition t = 0
    for (ix = 0; ix < nx; ix++)
      for (iy = 0; iy < ny; iy++)
        u0[ix*ny + iy] = (float)(ix * (nx - 1 - ix) * iy * (ny - 1 - iy)); 
    // boundary condition (x, y) 
    for (ix = 0; ix < nx; ix++) { // top and bottom
      u1[ix*ny] = u0[ix*ny];
      u1[ix*ny + ny - 1] = u0[ix*ny + ny - 1];
    }
    for (iy = 0; iy < ny; iy++) { // left and right
      u1[iy] = u0[iy];
      u1[(nx - 1)*ny + iy] = u0[(nx - 1)*ny + iy];
    }
    sx = width/nx;
    sy = height/ny;
    print("init "+u0[50*nx+50]+"\n");
  }
  /****************************************************************************
   *   (f(x,y)_n+1 - f(x,y)_n) / dt = gamma(d^2 f(x,y) / dx^2 + d^2 f(x,y) / dy^2)
   * where
   *     d^2 f(x,y) / dx^2 = ((f(x + dx,y) - f(x,y)) - (f(x,y) - f(x-dx,y))) / dx^2
   *     d^2 f(x,y) / dy^2 = ((f(x,y + dy) - f(x,y)) - (f(x,y) - f(x,y)-dy)) / dy^2
   ****************************************************************************/
  void update() {
    nn++;
    //nn %= 2;
    if((nn%2) == 0) update(u1,u0);
    else      update(u0,u1);
    
    if((nn % 30) == 0)print(nn+"  " +u1[50*nx+50]+"\n");
  }
  void update(float[] uu1, float [] uu2){
    int ix, iy, ixiy;

    for (ix = 1; ix < nx - 1; ix++) {
      for (iy = 1; iy < ny - 1; iy++) {
        ixiy = ix * ny + iy;
        uu2[ixiy] = uu1[ixiy] +
          cx * (uu1[ixiy + ny] + uu1[ixiy - ny] - 2.0 * uu1[ixiy]) +
          cy * (uu1[ixiy + 1] + uu1[ixiy - 1] - 2.0 * uu1[ixiy]);
        fill((int)(255 - (uu2[ixiy]/6.1e6*160+95)),255,255);  // HSB
        //fill((int)(uu2[ixiy]/7.0e6*255));  // black&white
        rect(ix*sx,iy*sy,sx,sy);
      }      
    }
  }
}
