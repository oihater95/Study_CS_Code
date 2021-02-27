#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <math.h>
#include <iostream>
#include <time.h>
#define SAMPLE 20000      // ���� ����
#define pi (3.141592)
using namespace std;

double snr = 0;            // Eb/No ����

int energy_sym = 1;         // Esym=A^2=1
float sigma = 0;        // �л�

double awgn_sig;          // AWGN ä�� ȯ��


double gaussian1();       //�־��� SNR�κ��� gaussian noise (array)����


int main()
{
	int i, sum; // sum�� Error ������ ����
	double n;   // AWGN ȯ��
	srand((unsigned int)time(NULL));
	double *sn1, *s1, *s2, *rn2, *rn1, *rx;
	sn1 = new double[SAMPLE];
	s1 = new double[SAMPLE];
	s2 = new double[SAMPLE];
	rn1 = new double[SAMPLE];
	rn2 = new double[SAMPLE];
	rx = new double[SAMPLE];


	ofstream error("error_table2.txt"); // BER �����ϱ� ���� ���� ����
	ofstream fout("noise signal2.dat");

	for (snr = 0; snr < 21; snr++)         // Eb/No�� 0~20���� ��ȭ ��Ű�� ���� �ݺ���
	{
		sum = 0;                     // Error ���� ���� ���� �ʱ�ȭ
		for (i = 0; i < SAMPLE; i++)
		{
			sn1[i] = (rand() % 2);          //�������� ��ȣ�� 0,1 ����
		}

		//���� ��ȣ�� ���� ���� �ϴ� ����
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
		//������ �������� ����
		for (i = 0; i < SAMPLE / 2; i++)
		{

			sigma = sqrt(energy_sym / (4 * pow(10, snr / 10)));
			n = sigma * gaussian1();

			rn1[i] = s1[i] + n;        // ���� ������ ��ȣ�� ������ ������
			n = sigma * gaussian1();
			rn2[i] = s2[i] + n;        // ���� ������ ��ȣ�� ������ ������
			if (snr == 2)
				fout << rn1[i] << "\t" << rn2[i] << endl;
		}

		//���Ŵܿ��� ���۵� ��ȣ�� ��ȣ�ϴ� ����
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

		// ���� ��ȣ�� ���ŵ� ��ȣ�� ���Ͽ� error ���� ����
		for (i = 0; i < SAMPLE; i++)
		{
			if (sn1[i] != rx[i])
			{
				sum++;
			}
		}

		// ������ error�� ���ð����� ������ BER Ȯ��e
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

// ���Ժ��� ����� ����
double gaussian1()
{
	double v1, v2, s;

	do
	{
		v1 = 2 * ((double)rand() / RAND_MAX) - 1;      // -1.0 ~ 1.0 ������ ��
		v2 = 2 * ((double)rand() / RAND_MAX) - 1;      // -1.0 ~ 1.0 ������ ��
		s = v1 * v1 + v2 * v2;
	} while (s >= 1 || s == 0);

	s = sqrt((-2 * log(s)) / s);
	return v1 * s;
}
