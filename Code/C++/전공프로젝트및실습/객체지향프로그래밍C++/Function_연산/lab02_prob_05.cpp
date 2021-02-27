#include <iostream>
using namespace std;


void swap_call_by_value(int a, int b)
{
	int temp = a;
	a = b;
	b = temp;
}
void swap_call_by_reference(int &a, int &b)
{
	int temp = a;
	a = b;
	b = temp;
}

void get_data(int &x, int &y)
{
	cout << "x 입력 : ";
	cin >> x;
	cout << "y 입력 : ";
	cin >> y;
}

int main() {
	
	int x; int y;
	get_data(x, y);
	cout << "swap_call_by_value 함수 사용 전 "<< endl << "x = " << x << ", y = " << y << endl;
	swap_call_by_value(x, y);
	cout << "swap_call_by_value 함수 사용 후"<< endl <<"x = " << x << ", y = " << y << endl<<endl;
	cout << "swap_call_by_reference 함수 사용 전"  << endl << "x = " << x << ", y = " << y << endl;
	swap_call_by_reference(x, y);
	cout << "swap_call_by_reference 함수 사용 후" << endl << "x = " << x << ", y = " << y << endl;


	return 0;

}
