#include <iostream>
#include <cmath>
#include <fstream>
#include <chrono>
#define PI 3.141592
using namespace std;

using ns = chrono::nanoseconds;
using get_time = chrono::steady_clock;

int main()
{
	double t, dt, T, xbar = 0, difft, integt, snr1;
	t = 0.0;
	dt = 0.001;
	T = 0.1;
	ofstream myout("integ.txt");

	double errorinpercent, theorm;
	auto start = get_time::now();
	for (t = 0; t<T-0.001; t += dt)
	{
		xbar += 2 * sin(2 * 100. * PI*t)*dt;
		theorm = (1. / (100.*PI))*(1 - cos(2 *100.* PI*t));
		myout << t << " " << xbar << " " << theorm << " " << 10*log(theorm/abs(theorm-xbar))<< endl;
	}
	auto end = get_time::now();
	auto integ = end - start;
	integt = chrono::duration_cast<ns>(integ).count();
	cout << "적분 경과시간: " << integt << "ns " << endl;

	
	errorinpercent = fabs(0.00173 - xbar) / 0.00173 * 100;
	cout << "dt " << dt << " x=0.00173 " << xbar << " error " << errorinpercent << "%\n";
	myout.close();


	return 0;
}