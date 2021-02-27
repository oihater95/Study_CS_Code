#include <iostream>
#include <random>
#include <fstream>
#include <ctime>
#include <cmath>
using namespace std;
#define PI 3.141592

double gaussian(double m, double sig, double a)
{
	return exp(-1 * (double)(pow((a-m),2)) / 2 * pow(sig,2)) / (sqrt(2 * PI)*sig);
}

int main()
{
	double trial, p, m, sum, x;
	double sig;
	trial = 100000;
	sum = 0;
	m = 35; // �ֻ��� 100�� �������� ���� ���
	sig = 5.4075 ; // �ֻ��� 100�� �������� ���� ǥ������
	p = 51; // 100�� �� ���ü� (100 ~ 600)
	
	int *arr = new int[trial]; // trial�� �õ�Ƚ��, trial��ŭ ������ �� ����
	int *ary = new int[p](); // p�� 100�� ���� ���ü� �ִ� ������ ��, 100~600�� ���� Ƚ�� ����
	ofstream fout("dice100_2.txt");
	
	for (int i = 0; i < trial; i++) // 100�� �� trial ���� ����
	{
		for (int j = 0; j < 10; j++) // 100�� ��
		{
			x = rand() % 6 + 1; // 1���� 6���� ����
			sum += x;
		}
		arr[i] = sum;
		sum = 0;
		
	}

	for (int i = 0; i < p; i++)
	{
		for (int j = 0; j < trial; j++)
		{
			if (arr[j] == i + 10)
			{
				ary[i]++;
			}
		}
		fout << i +10 << " " << (double)ary[i] / trial << endl;
	}
	fout.close();

	ofstream myout("gaussian_2.txt");
	for (int k = 10; k < 61; k++)
	{
		myout << k << " " << (double)gaussian(m, sig, k) << endl;
	}
	myout.close();

	delete[] arr;
	delete[] ary;
	
	getchar();


	return 0;
}