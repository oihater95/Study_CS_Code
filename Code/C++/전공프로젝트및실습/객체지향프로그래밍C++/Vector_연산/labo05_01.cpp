#include <iostream>
#include <cmath>
using namespace std;

void sqr(int *num)
{
	cout << "������> " << pow(*num, 2)<< endl;

}


int main() 
{
	int num1;
	cout << "input> ";
	cin >> num1;

	sqr(&num1);

	return 0;
}