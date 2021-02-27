#include <iostream>
#include <cmath>
using namespace std;


int main() {
	double x; double y;
	cout << "x 입력 : ";
	cin >> x;
	cout << "y 입력 : ";
	cin >> y;

	cout << "sqrt(double x) = " << sqrt(x) << endl; // x에 대한 양의 제곱근
	cout << "exp(double x) = " << exp(x) << endl; // 지수 e^x
	cout << "log10(double x) = " << log10(x) << endl; // 밑이 10인 로그
	cout << "cos(double x) = " << cos(x) << endl; // 삼각함수 cos(x)
	cout << "pow(double x, double y) = " << pow(x, y) << endl; // x^y
	cout << "fabs(double x) = " << fabs(x) << endl; // x의 절대값

	return 0;
}