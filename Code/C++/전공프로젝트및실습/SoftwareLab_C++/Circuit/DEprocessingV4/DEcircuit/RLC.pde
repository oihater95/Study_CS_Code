class RLC{
  RLC(){
    V = 48;
    R = 280;
    L = 100*1e-3;
    C = 0.4*1e-6;
    initialize();
  };
  RLC(float v, float r, float l, float c){
    V = v;
    R = r;
    L = l*1e-3;
    C = c*1e-6;
    initialize();
  }
  float V,R,L,C,dt,t=0;
  float vtp1,vt,vtm1; // v(t+dt), v(t), v(t-dt)
  int N,dn,n;
  void initialize(){
    vtp1 = vt = vtm1 = 0;
    t = 0;
    
    dt = 1./sqrt(abs(R/L*R/L - 4.0*1.0/L/C))*2.*PI/20.0;  // (omega/2pi)^-1 /20
    print("dt = "+dt+"\n");
    N = (int)(6e-3/dt);
    dn = width/N;
  }
  void update(){
    t += dt;
    vtp1 = ((2*vt-vtm1)-dt*(vt-vtm1)*R/L + dt*dt*(V-vt)/L/C);
    vtm1 = vt;
    vt = vtp1;
    print(vt+"\n");
    stroke(0,0,255);
    line(t/dt*dn,(1-vtm1/80)*height,(t/dt+1)*dn,(1-vt/80)*height);
    stroke(255,0,0);
    line(t/dt*dn,(1-analytic(t)/80)*height,
        (t/dt+1)*dn,(1-analytic(t+dt)/80)*height);
  }
  float analytic(float tt){
    return 48.-exp(-1400*tt)*(48*cos(4800*tt)+14*sin(4800*tt));
  }
};
