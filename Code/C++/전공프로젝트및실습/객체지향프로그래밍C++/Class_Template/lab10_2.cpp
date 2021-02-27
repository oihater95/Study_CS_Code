#include <iostream>
#include <vector>
#include <ctime>
using namespace std;



int main()
{
	srand((unsigned int)time(0));

	std::vector<int> vector1;
	std::vector<int> vector2;

	for (int i = 0; i < 10; i++)
	{
		vector1.push_back(rand() % 11);
		vector2.push_back(rand() % 21);
	}

	std::vector<int>::iterator iter1 = std::begin(vector1);
	std::vector<int>::iterator iter2 = std::begin(vector2);

	cout << "<vector 1>" << endl;
	
	for (int j = 0; j < 10; j++)
	{
		cout << *iter1 << " ";
		iter1++;
	}
	cout << endl;

	cout << "<vector 2>" << endl;

	for (int k = 0; k < 10; k++)
	{
		cout << *iter2 << " ";
		iter2++;
	}
	cout << endl << endl;

	int max = 0, temp = 0, min=0;
	iter1 = std::begin(vector1);

	for (int a = 0; a < 10; a++)
	{
		
		iter2 = std::begin(vector2);

		for (int b = 0; b < 10; b++)
		{
			temp = (*iter1 * *iter2);
			if (temp >= max)
			{
				max = temp;
			}
			iter2++;
		}
		
		iter1++;
	}
	
	iter1 = std::begin(vector1);
	temp = 0;
	for (int c = 0; c < 10; c++)
	{

		iter2 = std::begin(vector2);

		for (int d = 0; d < 10; d++)
		{
			temp = (*iter1 * *iter2);
			if (temp <= min)
			{
				min = temp;
			}
			iter2++;
		}

		iter1++;
	}

	cout << "ÃÖ´ñ°ª = " << max << endl;
	cout << "ÃÖ¼Ú°ª = " << min << endl;

	return 0;
}