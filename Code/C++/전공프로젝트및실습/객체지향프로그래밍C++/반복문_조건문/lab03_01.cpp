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
			cout << n << "은 짝수입니다." << endl;
		}
		else
		{
			cout << n << "은 홀수입니다." << endl;
		}
		cout << "number : ";
		cin >> n;

	}
		



	return 0;
}