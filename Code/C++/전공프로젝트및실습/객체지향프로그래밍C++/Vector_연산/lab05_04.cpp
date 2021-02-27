#include <iostream>
using namespace std;

int main()
{
	int *numbers;
	int size;
	bool flag = 1;
	while (flag)
	{
		cout << "Please enter number of values to process : ";
		cin >> size;
		int count = 0, cnt = 0;
		if (size > 0)
		{
			numbers = new int[size];
			cout << "Please enter numbers : ";
			for (int i = 0; i < size; i++)
			{
				cin >> numbers[i];
			}

			for (int j = 0; j < size; j++)
			{
				if (numbers[j] <= size)
				{
					continue;
				}
				else
				{
					count++;
				}
			}

			for (int k = 0; k < size - 1; k++)
			{
				for (int l = k+1; l < size; l++)
				{
					if (numbers[k] != numbers[l])
					{
						continue;
					}
					else
						cnt++;
				}
			}

			if (count == 0 && cnt == 0)
				cout << "True" << endl << endl;
			else
				cout << "False" << endl << endl;


		}
		else
		{
			cout << endl;
			break;
		}
		delete [] numbers;
	}
	return 0;
}