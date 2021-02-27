#include <iostream>
#include <cmath>
#include <fstream>
#define PI 3.141592
using namespace std;


double f1(double t)
{
	return sin(2 * PI * 100 * t);
}

double f2(double t)
{
	return 200 * PI*cos(2 * PI * 100 * t);
}

double f3(double t, double d)
{
	return(f1(t + d) - f1(t));
}

int main()
{
	double t, dt, T, xbar = 0;;
	t = 0.0;
	dt = 0.001;
	T = 0.1;
	ofstream fout("diff.txt");
	ofstream myout("integ.txt");

	for (t = 0; t<T ; t += dt )
	{
		fout << t << " " << f3(t, dt) << endl;
	}

	fout.close();

	for (t=0 ; t<T; t += dt)
	{
		xbar += sin(2*100*PI*t)*dt;
			myout << t << " " << xbar << endl;
	}

	myout.close();

	return 0;
}
