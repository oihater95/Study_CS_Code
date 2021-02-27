#include <iostream>
#include <cmath>
#include <fstream>
#include <ctime>
using namespace std;

double Poisson(double a, int x)
{
	double px = 1.0;
	for (int i = 0; i <= x; i++)
	{
		px *= (a / (double)i);
	}
	return px * exp(-a);
}

double factorial(double n)
{
	if (n > 0.0)
		return n * factorial(n - 1.0);
	else
		return 1.0;
}

int main()
{
	double p;
	int n, x;

	return 0;
}