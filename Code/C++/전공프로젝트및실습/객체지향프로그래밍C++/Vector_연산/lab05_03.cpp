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
	cout << "기본 Vector 값 : " << endl;
	for (unsigned i = 0; i < a.size(); i++)
	{
		a[i] = i+1;
		cout << setw(3) << a[i];

	}
	cout << endl << "함수 실행 후 Vector 값 : "<<endl;
	
	swap(a);
	for (unsigned i = 0; i < a.size(); i++)
	{
		
		cout << setw(3) << a[i];

	}
	cout << endl;

	return 0;
}