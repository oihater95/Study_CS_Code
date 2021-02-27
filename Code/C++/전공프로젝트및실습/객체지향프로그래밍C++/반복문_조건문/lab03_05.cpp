#include <iostream>
using namespace std;

int god(int a, int b)
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



int main()
{
	int a, b, t1, t2;
	cin >> a >> b;
	t1 = a, t2 = b;

	cout << "god(" << t1 << "," << t2 << ") = " << god(t1, t2) << endl;

	return 0;
}