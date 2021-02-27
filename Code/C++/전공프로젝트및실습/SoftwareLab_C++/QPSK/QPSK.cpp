#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <math.h>
#include <iostream>
#include <time.h>
#define SAMPLE 20000      // 샘플 개수
#define pi (3.141592)
using namespace std;

double snr = 0;            // Eb/No 지정

int energy_sym = 1;         // Esym=A^2=1
float sigma = 0;        // 분산

double awgn_sig;          // AWGN 채널 환경


double gaussian1();       //주어진 SNR로부터 gaussian noise (array)생성


int main()
{
	int i, sum; // sum은 Error 개수를 누적
	double n;   // AWGN 환경
	srand((unsigned int)time(NULL));
	double *sn1, *s1, *s2, *rn2, *rn1, *rx;
	sn1 = new double[SAMPLE];
	s1 = new double[SAMPLE];
	s2 = new double[SAMPLE];
	rn1 = new double[SAMPLE];
	rn2 = new double[SAMPLE];
	rx = new double[SAMPLE];


	ofstream error("error_table2.txt"); // BER 저장하기 위한 파일 생성
	ofstream fout("noise signal2.dat");

	for (snr = 0; snr < 21; snr++)         // Eb/No를 0~20까지 변화 시키기 위한 반복문
	{
		sum = 0;                     // Error 개수 저장 공간 초기화
		for (i = 0; i < SAMPLE; i++)
		{
			sn1[i] = (rand() % 2);          //랜덤으로 신호를 0,1 생성
		}

		//전송 신호를 위상 변조 하는 과정
		for (i = 0; i < SAMPLE; i = i + 2)
		{
			if ((sn1[i] == 0) && (sn1[i + 1] == 0))
			{
				if (i != 0)
				{
					s1[i / 2] = -0.707;
					s2[i / 2] = -0.707;
				}
				else
				{
					s1[i] = -0.707;
					s2[i] = -0.707;
				}
			}
			else if ((sn1[i] == 0) && (sn1[i + 1] == 1))
			{
				if (i != 0)
				{
					s1[i / 2] = -0.707;
					s2[i / 2] = 0.707;
				}
				else
				{
					s1[i] = -0.707;
					s2[i] = 0.707;
				}
			}
			else if ((sn1[i] == 1) && (sn1[i + 1] == 0))
			{
				if (i != 0)
				{
					s1[i / 2] = 0.707;
					s2[i / 2] = -0.707;
				}
				else
				{
					s1[i] = 0.707;
					s2[i] = -0.707;
				}
			}
			else
			{
				if (i != 0)
				{
					s1[i / 2] = 0.707;
					s2[i / 2] = 0.707;
				}
				else
				{
					s1[i] = 0.707;
					s2[i] = 0.707;
				}
			}
		}
		//잡음이 더해지는 과정
		for (i = 0; i < SAMPLE / 2; i++)
		{

			sigma = sqrt(energy_sym / (4 * pow(10, snr / 10)));
			n = sigma * gaussian1();

			rn1[i] = s1[i] + n;        // 위상 변조한 신호에 잡음이 더해짐
			n = sigma * gaussian1();
			rn2[i] = s2[i] + n;        // 위상 변조한 신호에 잡음이 더해짐
			if (snr == 2)
				fout << rn1[i] << "\t" << rn2[i] << endl;
		}

		//수신단에서 전송된 신호를 복호하는 과정
		for (i = 0; i < SAMPLE / 2; i++)
		{
			if (rn1[i] > 0)
			{
				rx[i * 2] = 1;
			}
			else
			{
				rx[i * 2] = 0;
			}

			if (rn2[i] > 0)
			{
				rx[i * 2 + 1] = 1;
			}
			else
			{
				rx[i * 2 + 1] = 0;
			}
		}

		// 원래 신호와 수신된 신호를 비교하여 error 개수 누적
		for (i = 0; i < SAMPLE; i++)
		{
			if (sn1[i] != rx[i])
			{
				sum++;
			}
		}

		// 누적된 error를 샘플개수로 나누어 BER 확인e
		if (i != 20)
		{
			error << (int)snr << "\t" << (double)sum / SAMPLE << "\n";
		}
		else
		{
			error << (int)snr << "\t" << (double)sum / SAMPLE << "\n";
		}
	}
	delete[] sn1;
	delete[] s1;
	delete[] s2;
	delete[] rn1;
	delete[] rn2;
	delete[] rx;
	fout.close();
	error.close();
	return 0;
}

// 정규분포 만드는 과정
double gaussian1()
{
	double v1, v2, s;

	do
	{
		v1 = 2 * ((double)rand() / RAND_MAX) - 1;      // -1.0 ~ 1.0 까지의 값
		v2 = 2 * ((double)rand() / RAND_MAX) - 1;      // -1.0 ~ 1.0 까지의 값
		s = v1 * v1 + v2 * v2;
	} while (s >= 1 || s == 0);

	s = sqrt((-2 * log(s)) / s);
	return v1 * s;
}
