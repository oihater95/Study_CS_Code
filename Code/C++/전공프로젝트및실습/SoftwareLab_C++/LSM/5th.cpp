// matrix_LSM.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
///
#include <iostream> // for getchar( )
#include <fstream> // for FILE
#include <cstdlib>  // for rand( )
#include <cmath>  // for exp( )
#include "myMatrix.h"
using namespace std;

int main()
{
	// data generation
	int N, i;
	N = 100;
	float* datax = new float[N];
	float* datay = new float[N];
	
	ifstream fth("5thdata.txt");
	
	for (i = 0; i < N; i++) {

		fth >> datax[i] >> datay[i];
	}
	fth.close();
	// LSM
	float A[36], B[6];
	for (i = 0; i < 36; i++) A[i] = 0.0;
	for (i = 0; i < 6; i++) B[i] = 0.0;
	for (i = 0; i < N; i++) {
		float x, x2, x3, x4, x5, x6, y, xy, x2y;
		x = datax[i]; x2 = x * x; x3 = x2 * x; x4 = x3 * x; x5 = x4 * x; x6 = x5 * x;
		y = datay[i]; xy = y * x; x2y = y * x2;
		A[0] += x5;          A[1] += x4;      A[2] += x3;     A[3] += x2;	A[4] += x;  	A[5] += 1.;		 B[0] += y;
		A[6] += x6;          A[7] += x5;      A[8] += x4;     A[9] += x3;	A[10] += x2;	A[11] += x;		 B[1] += xy;
		A[12] += x6*x;       A[13] += x6;     A[14] += x5;    A[15] += x4;	A[16] += x3;	A[17] += x2;	 B[2] += x2y;
		A[18] += x6 * x2;     A[19] += x6*x;  A[20] += x6;    A[21] += x5;	A[22] += x4;	A[23] += x3;	 B[3] += x2y * x;
		A[24] += x6 * x3;     A[25] += x6 * x2;  A[26] += x6*x;    A[27] += x6;	A[28] += x5;	A[29] += x4;	 B[4] += x2y * x2;
		A[30] += x6 * x4;     A[31] += x6 * x3;  A[32] += x6*x2;    A[33] += x6*x;	A[34] += x6;	A[35] += x5;	 B[5] += x2y * x3;
	}

	GaussElimination(6, A, B);

	cout << "y = " << B[0] << " x5 + " << B[1] << " x4 + " << B[2] << " x3 + " << B[3] << " x2 + " << B[4] << " x1 + " << B[5] << endl;

	getchar();

	return 0;
}

