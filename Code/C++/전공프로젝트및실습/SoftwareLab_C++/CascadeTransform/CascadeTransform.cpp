#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

void matrixmult(int, int, int, float*, float*, float*);
void showMatrix(int, int, float*);
void cascade(float*, int, float*, float*, float*, float*);
void reverse(float*CT, int N, int M, float *C);
void compress(float*, int, float *);

int main() {
	// Assignment 1
	float c0[4] = { 0.5,0.5,0.5,0.5 };
	float c1[4] = { 0.5,0.5,-0.5,-0.5 };
	float c2[4] = { 0.5,-0.5,-0.5,0.5 };
	float c3[4] = { 0.5,-0.5,0.5,-0.5 };
	float C[16] = { 0, };
	float CT[16] = { 0, };
	float CCT[16] = { 0, };

	// Assignment 2
	float a0[4] = { 100, 120, -4, 2 };
	float a1[4] = { 100, 20, 120, 32 };
	float a2[4] = { 10, 120, 108, 8 };
	float A0[4] = { 0, };
	float A1[4] = { 0, };
	float A2[4] = { 0, };
	float a0_i[4] = { 0, };
	float a1_i[4] = { 0, };
	float a2_i[4] = { 0, };
	float A0_c[4] = { 0, };
	float A1_c[4] = { 0, };
	float A2_c[4] = { 0, };

	cout << "C" << endl;
	cascade(C, 4, c0, c1, c2, c3);
	showMatrix(4, 4, C);
	cout << "\n" << "CT" << endl;
	reverse(CT, 4, 4, C);
	showMatrix(4, 4, CT);
	cout << "\n" << "CCT" << endl;
	matrixmult(4, 4, 4, C, CT, CCT);
	showMatrix(4, 4, CCT);

	cout << "\n" << "transform" << "\n" << "A0" << endl;
	matrixmult(4, 4, 1, C, a0, A0);
	showMatrix(4, 1, A0);
	cout << "\n" << "A1" << endl;
	matrixmult(4, 4, 1, C, a1, A1);
	showMatrix(4, 1, A1);
	cout << "\n" << "A0" << endl;
	matrixmult(4, 4, 1, C, a2, A2);
	showMatrix(4, 1, A2);

	cout << "\n" << "inverse" << "\n" << "a0" << endl;
	matrixmult(4, 4, 1, CT, A0, a0_i);
	showMatrix(4, 1, a0_i);
	cout << "\n" << "a1" << endl;
	matrixmult(4, 4, 1, CT, A1, a1_i);
	showMatrix(4, 1, a1_i);
	cout << "\n" << "a2" << endl;
	matrixmult(4, 4, 1, CT, A2, a2_i);
	showMatrix(4, 1, a2_i);

	cout << "\n" << "compression" << "\n" << "A0" << endl;
	compress(A0_c, 4, A0);
	showMatrix(4, 1, A0_c);
	cout << "\n" << "A1" << endl;
	compress(A1_c, 4, A1);
	showMatrix(4, 1, A1_c);
	cout << "\n" << "A2" << endl;
	compress(A2_c, 4, A2);
	showMatrix(4, 1, A2_c);

	cout << endl << "CT * A0" << endl;
	matrixmult(4, 4, 1, CT, A0_c, a0_i);
	showMatrix(4, 1, a0_i);
	cout << endl << "CT * A1" << endl;
	matrixmult(4, 4, 1, CT, A1_c, a1_i);
	showMatrix(4, 1, a1_i);
	cout << endl << "CT * A2" << endl;
	matrixmult(4, 4, 1, CT, A2_c, a2_i);
	showMatrix(4, 1, a2_i);
	ofstream myout;
	myout.open("assignment3.dat", ios::binary | ios::out);
	myout.write((char*)A0_c, 4 * sizeof(float));
	myout.write((char*)A1_c, 4 * sizeof(float));
	myout.write((char*)A2_c, 4 * sizeof(float));
	myout.close();

	float AA0[4], AA1[4], AA2[4];
	ifstream myin;
	myin.open("assignment3.dat", ios::binary | ios::in);
	myin.read((char*)AA0, 4 * sizeof(float));
	myin.read((char*)AA1, 4 * sizeof(float));
	myin.read((char*)AA2, 4 * sizeof(float));
	myin.close();

	float aa0[4], aa1[4], aa2[4];
	matrixmult(4, 4, 1, CT, AA0, aa0);
	matrixmult(4, 4, 1, CT, AA1, aa1);
	matrixmult(4, 4, 1, CT, AA2, aa2);
	cout << "\n" << "a0" << endl;
	showMatrix(4, 1, aa0);
	cout << "\n" << "a1" << endl;
	showMatrix(4, 1, aa1);
	cout << "\n" << "a2" << endl;
	showMatrix(4, 1, aa2);
	return 0;
}

void cascade(float*C, int M, float*a, float*b, float*c, float*d) {
	int k = 0;
	for (int i = 0; i < M; i++) {
		C[k] = a[i];
		k++;
	}
	for (int i = 0; i < M; i++) {
		C[k] = b[i];
		k++;
	}for (int i = 0; i < M; i++) {
		C[k] = c[i];
		k++;
	}for (int i = 0; i < M; i++) {
		C[k] = d[i];
		k++;
	}
}

void reverse(float*CT, int N, int M, float *C) {
	int n, m;
	int k = 0;
	for (n = 0; n < N; n++) {
		for (m = 0; m < M; m++) {
			CT[m*N + n] = C[n*M + m];
		}
	}
}

void compress(float *AC, int N, float *A) {
	for (int i = 0; i < N; i++) {
		AC[i] = A[i];
	}

	float min = A[0];
	int id;
	for (int i = 1; i < N; i++) {
		if (A[i] <= min) {
			min = A[i];
			id = i;
		}
	}
	AC[id] = 0;

	float min2 = A[0];
	int id2;
	for (int i = 1; i < N; i++) {
		if (AC[i] != 0) {
			if (A[i] <= min2) {
				min2 = A[i];
				id2 = i;
			}
		}
	}
	AC[id2] = 0;
}

/*void transform(int K, float*A, int N, int M, float*C, float*a) {
for (int i = 0; i < N; i++) {
for (int j = 0; j < M; j++) {
float sum = 0;
for(int k = 0; k<K;k++) sum +=
}
}
}*/


void matrixmult(int N, int K, int M, float*C, float*D, float*E) {
	int n, k, m;
	for (n = 0; n < N; n++) {
		for (m = 0; m < M; m++) {
			float sum = 0;
			for (k = 0; k < K; k++) sum += C[n*K + k] * D[k*M + m];
			E[n*M + m] = sum;
		}
	}
}

void showMatrix(int n, int m, float* F) {
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) cout << F[i*m + j] << "\t";
		cout << "\n";
	}
}