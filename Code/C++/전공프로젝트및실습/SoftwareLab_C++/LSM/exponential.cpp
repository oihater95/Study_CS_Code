#include <iostream>
#include <fstream>
#include <cmath>
#include "myMatrix.h"
using namespace std;

void main()
{
	float A[4], b[2];
	ifstream xxx("datae.txt");
	int N;
	xxx >> N;
	float* dataX = new float[N];
	float* dataY = new float[N];
	for (int i = 0; i < N; i++)
	{
		xxx >> dataX[i] >> dataY[i];
	}
	for (int i = 0; i < 4; i++) A[i] = 0;
	b[0] = b[1] = 0;
	for (int i = 0; i < N; i++)
	{
		A[0] += dataX[i];
		A[1] += 1.;
		b[0] += log(fabs(dataY[i]));
		A[2] += pow(dataX[i], 2);
		A[3] += dataX[i];
		b[1] += dataX[i] * log(fabs(dataY[i]));
	}
	GaussElimination(2, A, b);
	cout << "log(y) = " << b[0] << "x + log(" << b[1] << ")" << endl;
	cout << "y = " << exp(b[1]) << " * exp(" << b[0] << "x) " << endl;
	getchar();
	return;
}