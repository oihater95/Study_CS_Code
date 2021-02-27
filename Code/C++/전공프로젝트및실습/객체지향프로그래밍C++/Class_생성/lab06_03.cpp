#include <iostream>
#include <vector>
using namespace std;

int fibonacci(int n)
{
	
	
		if (n == 0)
		{
			return 0;
		}
		else if (n == 1)
		{
			return 1;
		}
		else
			return fibonacci(n-1) + fibonacci(n-2);


}

int main()
{
	int n;

	cout << "n : ";
	cin >> n;

	int* p = new int[n];
	
	for (int i = 0; i < n; i++)
	{
		p[i]= fibonacci(i);
	}

	

	for (int j = 0; j < n; j++)
	{
		cout << p[j] << " ";
	}
	cout << endl;

	delete [] p;
	return 0;
}