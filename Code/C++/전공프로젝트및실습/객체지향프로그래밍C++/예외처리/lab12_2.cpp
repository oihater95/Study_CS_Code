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
			cout << "���� list�� " << cnt << "�� ũ�⸦ ������ �ִ�." << endl;
			break;
		}
		cnt++;
	}

	return 0;
}