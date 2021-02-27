#include <iostream>
#include <cmath>
#include <fstream>
#include <chrono>
#define PI 3.141592
using namespace std;

using ns = chrono::nanoseconds;
using get_time = chrono::steady_clock;

double f1(double t)
{
	return 2.*sin(2 * PI * 100. * t);
}

double f2(double t)
{
	return 400. * PI*cos(2 * PI * 100. * t);
}

double f3(double t, double d)
{
	return(f1(t + d) - f1(t))/d;
}

int main()
{
	double t, dt, T, xbar = 0, difft, integt, snr2;
	t = 0.0;
	dt = 0.001;
	T = 0.1;
	ofstream fout("diff.txt");
	
	auto start = get_time::now();
	for (t = 0; t<T; t += dt)
	{
		fout << t << " " << f2(t) << " " << f3(t, dt) << " " << 10*log(f2(t)/abs(f2(t)-f3(t, dt))) << endl;
	}
	auto end = get_time::now();
	auto diff = end - start;
	difft = chrono::duration_cast<ns>(diff).count();
	cout << "미분 경과시간: " << difft << "ns " << endl;


	fout.close();

	
	return 0;
}
