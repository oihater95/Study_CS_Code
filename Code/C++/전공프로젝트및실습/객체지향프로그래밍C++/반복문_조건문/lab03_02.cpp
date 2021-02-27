#include <iostream>
using namespace std;

int main()
{
	int num;
	cout << "number : ";
	cin >> num;

	int sum=0, a=1;

	while (a <= num)
	{
		sum += a ;
		a++;

	}

	cout << sum << endl;

	return 0;
}

