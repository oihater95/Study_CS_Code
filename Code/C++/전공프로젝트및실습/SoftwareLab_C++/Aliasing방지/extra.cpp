#include <iostream>
#include <fstream>
#include <cmath>
#define PI 3.141592
using namespace std;

int main()
{
	ofstream fout("no aliasing2.txt");
	if (!fout)
	{
		cout << "Cannot open no aliasing2.txt file.\n";
		return -1;
	}

	double t, dt, T, sint;
	double fc = 1000, fo = 100, fs = 10000; // sampling frequency가 2200 크면 aliasing 방지
	dt = 1. / fs;
	T = 10. / 220;
	for (t = 0; t < T; t += dt)
	{
		sint = cos(2 * PI * fc * t + 0.2 * fc *  sin(2 * PI*fo*t));
		fout << t << " " << sint << endl;
	}


	fout.close();

	return 0;
}