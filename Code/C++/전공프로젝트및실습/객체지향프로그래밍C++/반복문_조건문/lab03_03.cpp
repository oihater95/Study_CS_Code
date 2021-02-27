#include <iostream>
using namespace std;

int main()
{
	int m, sum = 0, a = 1;
	cout << "number : ";
	cin >> m;

	while (a <= m)
	{
		if (a%2 == 1)
		{
			if (a % 3 != 0)
			{
				sum += a;
			}
		}
		
		a++;
	}

	cout << "sum : " << sum << endl;

	return 0;
}