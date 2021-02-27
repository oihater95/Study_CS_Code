#include <iostream>
#include <fstream>
#include <ctime>
#include <iomanip>

using namespace std;

int main()
{
	srand((unsigned int) time (NULL));

	ofstream fout;
	fout.open("temp.txt");
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			fout << setw(3) << rand() % 101;
			cout << setw(3) << rand() % 101;
		}
		fout << endl;
		cout << endl;

	}
	fout.close();
	return 0;
}