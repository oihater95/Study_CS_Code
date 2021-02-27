#include <iostream>
#include <exception>
#include <fstream>
#include <ctime>
#include <iomanip>
#include <vector>
#include <string>
using namespace std;

int main()
{
	srand((unsigned int)time(NULL));

	ofstream fout;
	fout.open("temp.txt");
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			fout << setw(3) << rand() % 101;
			
		}
		fout << endl;
		

	}
	fout.close();

	ifstream fin;
	
	string filename;
	cout << "파일 이름 : ";
	cin >> filename;
	
	try
	{
		if (filename != "temp.txt")
		{
			throw filename;
		}

		else
			fin.open(filename);

	}
	catch (string filename)
	{
		cout << "File " << filename << " not found"  << endl;
	}


	vector <vector<int>> vec;
	int num=0;
	for (int i = 0; i < 10; i++)
	{
		vector<int> a;
		vec.push_back(a);

		for (int j = 0; j < 10; j++)
		{
			fin >> num;
			vec[i].push_back(num);

		}
		
	}

	int row, col;
	cout << "출력할 행 크기 : ";
	cin >> row;
	cout << "출력할 열 크기 : ";
	cin >> col;

	try
	{

		for (int a = 0; a < row; a++)
		{
			for (int b = 0; b < col; b++)
			{

				int t;
				if (a >= 10)
				{
					t = a;
					throw t;
				}
				else if (b >= 10)
				{
					t = b;
					throw t;
				}
				else
				{
					cout << setw(3) << vec[a][b];
				}

			}

			cout << endl;
		}



	}
	catch (int t)
	{
		cout << endl;
		cout << "Invalid vector<T> subscript" << endl;
	}


	return 0;
}