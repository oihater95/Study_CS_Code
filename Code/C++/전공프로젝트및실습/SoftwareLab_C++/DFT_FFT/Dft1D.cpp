#include"Dft1D.h"

#include <math.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
//#include "complex.h"
#include "fft1D.hpp"
#include"Fft1D.hpp"
#define FORWARD  1
#define INVERSE -1
#define PI 3.141592
DFT::DFT(Real *data, int Nn)
{
	N = Nn;
	InitializeDFT();
	for (int i = 0; i < N; i++)  *(x + i) = complex<Real>(*(data + i), 0.0);
}

DFT::DFT(int Nn)
{
	N = Nn;
	InitializeDFT();
}

void DFT::InitializeDFT()
{
	x = new complex<double>[N];
	X = new complex<double>[N];
	W = new complex<double>[N];
	Real pi2N = 3.141592 * 2.0 / (Real)N;

	NU = 0; int k = 1;
	while (k != N) { k *= 2; NU += 1; }
	for (int i = 0; i < N; i++)   W[i] = complex<Real>(cos(-pi2N * (Real)i), sin(-pi2N * (Real)i));

}
DFT::~DFT()
{
	delete x;
	delete X;
	delete W;
}

void DFT::ForwardDFT(){
	complex<double> z1(0, 1);
	
	for (long k= 0; k < N; k++)
	{
		//complex<double> sum;
		for (long n = 0; n < N; n++)
		{
			X[k] += x[n] * exp(z1*(-2 * PI*k*n / N));
			
		}

		//X[k] = sum;
		
	}

}

void DFT::InverseDFT() {
	complex<double> z1(0, 1);
	for (long n = 0; n < N; n++)
	{
		//complex<double> sum;
		for (long k = 0; k < N; k++)
		{
			x[n] +=(1./N)*(X[k] * exp(z1*(2 * PI*k*n / N)));
		}

		//X[k] = sum;

	}

}
