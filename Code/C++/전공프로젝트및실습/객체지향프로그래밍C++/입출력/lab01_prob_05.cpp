#include <iostream>
using namespace std;

void get_two_numbers(int& a, int& b);
int get_operator();
int calc_sum_a_to_b(int a, int b);
int calc_sum_even_a_to_b(int a, int b);
int calc_gcd_a_to_b(int a, int b);

int main()
{
	int a, b, oper, result=0;


	while (1)
	{
		get_two_numbers(a, b);
		oper = get_operator();

		switch (oper)
		{
		case 0:
		{
			cout << "프로그램 종료" << endl;
			break;
		}
		case 1:
		{
			result= calc_sum_a_to_b(a, b);
			break;
		}
		case 2:
		{	result = calc_sum_even_a_to_b(a, b);
		break;
		}
		case 3:
		{
			result = calc_gcd_a_to_b(a, b);
			break;
		}
		default:
			cout << "output>" << result << endl << endl;
			break;
		}


		return 0;
	}
}

	void get_two_numbers(int& a, int& b)
{
	
	cout << "두 정수 a, b를 입력하시오 : ";
	cin >> a >> b;

}

int get_operator()
{
	int a;
	cout << "1 2 3 0" << endl << "input>";
	cin >> a;
	return a;

}

int calc_sum_a_to_b(int a, int b)
{
	int sum=0;
	if (a < b)
	{
		sum += a;
		return calc_sum_a_to_b(++a,b);

	}
	else
		return sum += b;
}

int calc_sum_even_a_to_b(int a, int b)
{
	int sum2=0;
	
	while (a!=b)
	{
		if (a % 2 == 0)
		{
			sum2 += a;

		}
		else
			a++;
		if (b % 2 != 0)
			b--;
		

	}
	return sum2 += b;
}

int calc_gcd_a_to_b(int a, int b)
{
	int temp, g;
	bool x = 1;
	while (x)
	{
		if (a%b != 0)
		{
			temp = a;
			a = b;
			b = temp % a;

		}
		else
		{
			g = b;
			x = 0;
		}
	}
	return g;
}