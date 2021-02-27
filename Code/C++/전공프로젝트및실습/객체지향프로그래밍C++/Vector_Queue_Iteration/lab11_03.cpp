#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int movex(int x, int num)
{
	x++;
	if (x == num)
		return 0;
	else
		return x;
}

int movey(int y, int num)
{
	y--;
	if (y == -1)
		return num - 1;
	else
		y;
}

int main()
{
	int num;
	cout << "홀수 숫자를 하나 입력해 주세요 : ";
	cin >> num;
	int** array = new int*[num];
	for (int i = 0; i < num; i++)
	{
		array[i] = new int[num];
		for (int k = 0; k < num; k++) 
		{
			array[i][k] = 0;
		}
	}
	int cnt = 1;
	int x = num / 2;
	int y = 0;
	int newx, newy;
	while (cnt != num * num + 1)
	{
		array[y][x] = cnt;
		newx = movex(x, num);
		newy = movey(y, num);
		if (array[newy][newx] != 0)
		{
			y++;
		}
		else
		{
			x = newx;
			y = newy;
		}
		cnt++;
	}


	for (int i = 0; i < num; i++)
	{
		for (int k = 0; k < num; k++) 
		{
			cout << "   " << array[i][k];
		}
		cout << endl;
	}


	return 0;
}
