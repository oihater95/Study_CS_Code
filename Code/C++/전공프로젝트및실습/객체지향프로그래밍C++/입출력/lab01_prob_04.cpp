#include <iostream>
using namespace std;

int main()
{
	int a, b, temp = 0;
	cout << "Please enter two integer values: " << endl;
	cout << "A : ";
	cin >> a;
	cout << "B : ";
	cin >> b;

	temp = b;
	b = a;
	a = temp;

	cout << "value of A is : " << a << endl;
	cout << "value of B is : " << b << endl;

	return 0;

}
