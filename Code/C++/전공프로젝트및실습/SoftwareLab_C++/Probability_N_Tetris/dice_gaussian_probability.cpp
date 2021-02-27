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
	m = 35; // 주사위 100번 던졌을때 합의 평균
	sig = 5.4075 ; // 주사위 100번 던졌을때 합의 표준편차
	p = 51; // 100번 합 샘플수 (100 ~ 600)
	
	int *arr = new int[trial]; // trial은 시도횟수, trial만큼 시행한 값 저장
	int *ary = new int[p](); // p는 100번 던져 나올수 있는 샘플의 수, 100~600이 나온 횟수 저장
	ofstream fout("dice100_2.txt");
	
	for (int i = 0; i < trial; i++) // 100번 합 trial 마다 저장
	{
		for (int j = 0; j < 10; j++) // 100번 합
		{
			x = rand() % 6 + 1; // 1부터 6까지 랜덤
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