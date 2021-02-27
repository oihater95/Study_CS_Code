#include <iostream>
#include <iomanip>
#include <cmath>
#define PI 3.141592
using namespace std;

double fxy(double x, double y);
double dfxydx(double x, double y, double dx);
double dfxydy(double x, double y, double dy);
double EE(double, double, double, double);

int main()
{
	double psi = 0.001, eta = 0.000001;
	double dx = 0.01, dy = 0.01;
	double xi0 = 0.02, yi0 = 0.02;
	double xi1 = 0.3, yi1 = 0.3;
	int iteration = 0;
	cout << "x0 : " << xi0 << " , " << "y0 : " << yi0 << endl;
	cout << "x1 : " << xi1 << " , " << "y1 : " << yi1 << endl;

	while (EE(xi0, yi0, xi1, yi1) > eta && iteration < 1000)
	{
		
		xi0 = xi1;
		yi0 = yi1;
		xi1 -= psi * dfxydx(xi0, yi0, dx);
		yi1 -= psi * dfxydy(xi0, yi0, dy);
		iteration++;
	}
	cout << iteration << "-th E = " << EE(xi0, yi0, xi1, yi1) << endl;
	cout << "min : " << fxy(xi1, yi1) << " at " << "( " << xi1 << ", " << yi1 << " )"<< endl << endl;

	xi1 = 0.05, yi1 = 0.01;
	xi0 = 0.5, yi0 = 0.05;
	iteration = 0;
	cout << "x0 : " << xi0 << " , " << "y0 : " << yi0 << endl;
	cout << "x1 : " << xi1 << " , " << "y1 : " << yi1 << endl;

	while (EE(xi0, yi0, xi1, yi1) > eta && iteration < 1000)
	{
		xi0 = xi1;
		yi0 = yi1;
		xi1 += psi * dfxydx(xi0, yi0, dx);
		yi1 += psi * dfxydy(xi0, yi0, dy);
		iteration++;
	}
	cout << iteration << "-th E = " << EE(xi0, yi0, xi1, yi1) << endl;
	cout << "max : " << fxy(xi1, yi1) << " at " << "( " << xi1 << ", " << yi1 << " )" << endl << endl;

	cout << "psi:" << psi << " eta:" << eta << " dx:" << dx << " dy:" << dy << endl;

	getchar();

	return 0;
}

double fxy(double x, double y)
{
	return sin(2*PI*x)*sin(2*PI*2*y);
}

double dfxydx(double x, double y, double dx)
{
	return (fxy(x + dx, y) - fxy(x, y)) / dx;
}

double dfxydy(double x, double y, double dy)
{
	return  (fxy(x, y + dy) - fxy(x, y)) / dy;
}

double EE(double x0, double y0, double x1, double y1)
{
	return sqrt(pow((x0 - x1), 2) + pow((y0 - y1), 2));
}