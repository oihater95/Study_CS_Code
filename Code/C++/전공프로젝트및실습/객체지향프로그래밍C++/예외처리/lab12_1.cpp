#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector<int> list{ 10,20,30,40,50 };
	int num;

	while (1)
	{
		cout << "출력 할 숫자의 수 : ";
		cin >> num;
		try
		{
			if (num > 5)
			{
				throw num;
			}
			

			for (int i = 0; i < num; i++)
			{
				cout << list[i] << " ";
			}
			cout << endl;
			break;
			
		}
		catch (int num) 
		{
			cout << "Index is out of range. Please try again." <<endl;
		}
	}

	return 0;
}