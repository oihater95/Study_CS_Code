#include <iostream>
#include <string>
using namespace std;

int main()
{
	string city, area, street, building, address;

	cout << "�� : ";
	cin >> city;
	cout << "�� : ";
	cin >> area;
	cout << "�� : ";
	cin >> street;
	cout << "�ǹ��� : ";
	cin >> building;

	address += city;
	address += area;
	address += street;
	address += building;

	cout << endl << "�� �ּ� : " << address << endl;

	return 0;
}
