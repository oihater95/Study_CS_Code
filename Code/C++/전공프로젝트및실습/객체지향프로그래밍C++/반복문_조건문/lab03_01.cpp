#include <iostream>
using namespace std;

int main()
{
	int n;
	cout << "number : ";
	cin >> n;
	
	while (n >= 0)
	{ 
		if (n % 2 == 0)
		{
			cout << n << "�� ¦���Դϴ�." << endl;
		}
		else
		{
			cout << n << "�� Ȧ���Դϴ�." << endl;
		}
		cout << "number : ";
		cin >> n;

	}
		



	return 0;
}