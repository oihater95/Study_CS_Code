#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

int main()
{
	srand((unsigned int)time(0));
	
	int length = rand() % 100;
	
	int *list = new int[length];

	for (int i = 0; i < length; i++)
	{
		list[i] = i+1;
	}

	int cnt = 1;
	
	while (1)
	{
		
		try
		{
			if (cnt > length)
			{
				throw cnt;
			}
		}
		
		catch (int cnt)
		{
			cout << "현재 list는 " << cnt << "의 크기를 가지고 있다." << endl;
			break;
		}
		cnt++;
	}

	return 0;
}