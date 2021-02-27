#include <iostream>
#include <fstream>
#include <cmath>
#define PI 3.141592
using namespace std;

int main()
{
	ofstream fout("no aliasing.txt");
	if (!fout)
	{
		cout << "Cannot open no aliasing.txt file.\n";
		return -1;
	}

	double t, dt, T, sint;
	double fc = 1000, fo = 100, fs = 8000; // sampling frequency가 2200 크면 aliasing 방지
	dt = 1. / fs;
	T = 10. / 220;
	for (t = 0; t < T; t += dt)
	{
		sint = sin(2 * PI* fo *t) * cos(2 * PI*fc*t);
		fout << t << " " << sint << endl;
	}


	fout.close();

	return 0;
}

