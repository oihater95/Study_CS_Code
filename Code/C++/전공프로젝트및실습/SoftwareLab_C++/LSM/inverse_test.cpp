#include <iostream>
#include <fstream>
#include "myMatrix.h"
using namespace std;

void main()
{
	float A[9], b[3];
	ifstream xxx("data2.txt");
	int N;
	xxx >> N;
	float *datax = new float[N];
	float *datay = new float[N];
	for (int i = 0; i < N; i++)
	{
		xxx >> datax[i] >> datay[i];
	}

	for (int j = 0; j < 9; j++)
	{
		A[j] = 0;
	}
	b[0] = b[1] = b[2] = 0;

	for (int k = 0; k < N; k++)
	{
		float x, x2, x3, x4, x5, y, xy, x2y;
		x = datax[k]; x2 = x * x; x3 = x2 * x; x4 = x3 * x; 
		y = datay[k]; xy = x * y; x2y = x2 * y;
		A[0] += x2 ; A[1] += x; A[2] += 1.; b[0] += datay[k];
		A[3] += x3; A[4] += x2; A[5] += x; b[1] += xy;
		A[6] += x4; A[7] += x3; A[8] += x2; b[2] += x2y;
	}

	GaussElimination(3, A, b);
	cout << "y = " << b[0] << "x2  + " << b[1] << "x + " << b[2] <<endl;
	getchar();
	
}
//y =  -1.17745x2  + 6.13387x + 3.22053