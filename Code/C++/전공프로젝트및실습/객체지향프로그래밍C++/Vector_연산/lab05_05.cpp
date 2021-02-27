#include <iostream>
#include <vector>
#include <ctime>
#include <iomanip>
using namespace std;


void matrix(vector<vector<int>>&arr, int row, int col)
{
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			arr[i][j] = rand() % 19 - 9;
			
		}
	}
}

void printmatrix(vector<vector<int>>&arr, int row, int col)
{
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			cout << setw(5) << arr[i][j];
		}
		cout << endl;
	}
}

void multimatrix(vector<vector<int>>&arr1, vector<vector<int>>&arr2, int row1, int col1, int row2, int col2)
{
	vector<vector<int>> arr_temp(row1, vector<int>(col2,0));
	int sum_temp = 0;
	if (col1 == row2)
	{
		for (int i = 0; i < row1; i++)
		{
			for (int j = 0; j < col2; j++)
			{
				for (int k = 0; k < col1; k++)
				{
					sum_temp = sum_temp + arr1[i][k] * arr2[k][j];
				}
				arr_temp[i][j] = sum_temp;
				sum_temp = 0;
			}
		}
		printmatrix(arr_temp, row1, col2);
	}
	else
		cout << "두 행렬을 곱할 수 없습니다." << endl;

}

int main()
{
	srand((unsigned int)time(NULL));
	int row1 , col1 , row2 , col2 ;
	
	cout << "A의 행, 열의 크기를 입력해주세요 : ";
	cin >> row1 >> col1;
	
	cout << "B의 행, 열의 크기를 입력해주세요 : ";
	cin >> row2 >> col2;
	cout << endl << endl;

	vector<vector<int>>arr1(row1, vector<int>(col1));
	vector<vector<int>>arr2(row2, vector<int>(col2));

	cout << "A 행렬 : " << endl;
	matrix(arr1, row1, col1);
	printmatrix(arr1, row1, col1);
	cout << endl << endl;

	cout << "B 행렬 : " << endl;
	matrix(arr2, row2, col2);
	printmatrix(arr2, row2, col2);
	cout << endl << endl;

	cout << "AB 곱행렬 : " << endl;
	multimatrix(arr1, arr2, row1, col1, row2, col2);

	return 0;
}