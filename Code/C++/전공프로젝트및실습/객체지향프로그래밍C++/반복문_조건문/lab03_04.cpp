#include <iostream>
using namespace std;

int main()
{
	int dan, a=1;
	bool b=1;

	

	while (b)
	{
		cout << "number : ";
		cin >> dan;
		if (dan <= 9 && dan >=1)
		{
			while (a <= 9)
			{
				cout << dan << "*" << a << " = " << dan * a << "  ";
				a++;
			}
			cout << endl;
			a = 1;
			continue;

		}
		else
			b=0;
	}
	return 0;
}