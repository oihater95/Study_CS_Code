#include <iostream>
using namespace std;

void print_DOB(int year = 2000, int month = 1, int day = 1) {
	cout << "나의 생년월일은 " << year << "년 " << month << "월 " << day << "일 입니다." << endl;
}

int main() {
	
	print_DOB();

	int year, month, day;
	cout << "year 입력 : ";
	cin >> year;
	cout << "month 입력 : ";
	cin >> month;
	cout << "day 입력 : ";
	cin >> day;

	print_DOB(year, month, day);

	return 0;
}