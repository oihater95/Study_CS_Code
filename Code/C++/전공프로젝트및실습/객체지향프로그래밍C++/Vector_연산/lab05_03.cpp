#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

void swap(vector<int> &a)
{
	for (unsigned i = 0; i < a.size(); i++)
	{
		a[i] = a.size() - i;
		
	}
}

int main()
{
	vector <int> a(10);
	cout << "�⺻ Vector �� : " << endl;
	for (unsigned i = 0; i < a.size(); i++)
	{
		a[i] = i+1;
		cout << setw(3) << a[i];

	}
	cout << endl << "�Լ� ���� �� Vector �� : "<<endl;
	
	swap(a);
	for (unsigned i = 0; i < a.size(); i++)
	{
		
		cout << setw(3) << a[i];

	}
	cout << endl;

	return 0;
}