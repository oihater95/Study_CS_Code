#include <iostream>
#include <string>
using namespace std;


void swap(string *str)
{

	cout << "input> ";
	cin >> *str;

}



int main()
{
	string str = "This is default value";
	cout << "�⺻�� ���> " << str << endl;

	swap(&str);

	cout << "��ȯ�� �� ���> " << str << endl;
	return 0;
}