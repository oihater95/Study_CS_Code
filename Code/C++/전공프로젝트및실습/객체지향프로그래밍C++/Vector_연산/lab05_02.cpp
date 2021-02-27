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
	cout << "기본값 출력> " << str << endl;

	swap(&str);

	cout << "변환된 값 출력> " << str << endl;
	return 0;
}