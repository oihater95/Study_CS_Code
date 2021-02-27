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

int add_mult(int x, int y, int z)
{
	return mult(sum(x, y), z);
 
}

double mult_div(int x, int y, int z)
{
	return idiv(mult(x, y), z);

}

int add_mult_add(int x, int y, int z)
{
	return mult(sum(x, y), sum(y, z));

}

double sub_div_sub(int x, int y, int z)
{
	return idiv(sub(x, y), sub(x, z));

}

int main()
{
	int x, y, z;

	cout << "x 입력 : ";
	cin >> x;
	cout << "y 입력 : ";
	cin >> y;
	cout << "z 입력 : ";
	cin >> z;

	cout << "(x + y) * z = " << add_mult(x, y, z) << endl;
	cout << "(x * y) / z = " << mult_div(x, y, z) << endl;
	cout << "(x + y) * (y + z) = " << add_mult_add(x, y, z) << endl;
	cout << "(x - y) / (x - z) = " << sub_div_sub(x, y, z) << endl;

	return 0;
}

