#include <iostream>
using namespace std;

int sum(int x, int y)
{
	return x + y;
}

int sub(int x, int y)
{
	return x - y;
}

int mult(int x, int y)
{
	return x * y;
}

double idiv(int x, int y)
{
	return (double)x / (double)y;

}

int main()
{
	int x, y;

	cout << "x �Է� : ";
	cin >> x;
	cout << "y �Է� : ";
	cin >> y;

	cout << "x + y = " << sum(x, y) << endl;
	cout << "x - y = " << sub(x, y) << endl;
	cout << "x * y = " << mult(x, y) << endl;
	cout << "x / y = " << idiv(x, y) << endl;

	return 0;
}

