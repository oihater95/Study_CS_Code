#include <iostream>
#include "myMatrix.h"
using namespace std;
void scalarmult(int n, int m, float a, float *b, float *c){
	int N = n*m;
    for(int i=0;i<N;i++) c[i] = a*b[i];
}
void matrixadd(int n, int m, float *a, float *b, float *c){
	int N = n*m;
	for (int i = 0; i<N; i++) c[i] = a[i]+b[i];
}  
// (N by K) C X (K by M) D = (N by M) E 
void matrixmult(int N, int K, int M, float*C, float*D, float*E) {
	int n, k, m;
	for (n = 0; n < N; n++)
		for (m = 0; m < M; m++) {
			float sum = 0;
			for (k = 0; k < K; k++) sum += C[n*K + k] * D[k*M + m];
			E[n*M + m] = sum;
		}
}
// Solve equation Av = b               
// return  0 when solution exists,
//        -1 when solution does not exist.
//   A ==> indentity matrix
//   b ==> v (the solution)
int GaussElimination(int N, float *a, float *b)
{
	float temp, aii, aji;
	int i, j, k;
	//showequation(N, a, b);
	for (i = 0; i<N; i++) {
		aii = a[i*N + i];
		if (aii == 0.0) return -1; // 부정/불능 여기 더 할 일 있음
								   // i-th row를 aii로 모두 나누기
		for (k = i; k<N; k++) a[i*N + k] /= aii;
		b[i] /= aii;
		// 다른 row들의 i번째 항을 모두 0으로 만들기
		for (j = 0; j<N; j++) {
			if (i != j) {
				aji = a[j*N + i];
				for (k = i; k<N; k++) a[j*N + k] -= a[i*N + k] * aji;
				b[j] -= b[i] * aji;
			}// if(i!=j)
		} // other rows
		//showequation(N, a, b);
	}
	return 0;
}
void showMatrix(int n, int m, float* F) {
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) cout << F[i*m + j] << "\t";
		cout << "\n";

	}
}
void showMatrix(char*name, int n, int m, float* F) {
	cout << name << endl;
	showMatrix(n, m, F);
}
// show N X N matrix
void showequation(int N, float *a, float *b)
{
	int i, j;
	for (i = 0; i<N; i++)
	{
		for (j = 0; j<N; j++) cout << a[i*N + j] << "\t";
		cout << b[i];
	}
	cout << "\n";
}