#include <iostream>
#include <cmath>
using namespace std;


int main() {
	double x; double y;
	cout << "x �Է� : ";
	cin >> x;
	cout << "y �Է� : ";
	cin >> y;

	cout << "sqrt(double x) = " << sqrt(x) << endl; // x�� ���� ���� ������
	cout << "exp(double x) = " << exp(x) << endl; // ���� e^x
	cout << "log10(double x) = " << log10(x) << endl; // ���� 10�� �α�
	cout << "cos(double x) = " << cos(x) << endl; // �ﰢ�Լ� cos(x)
	cout << "pow(double x, double y) = " << pow(x, y) << endl; // x^y
	cout << "fabs(double x) = " << fabs(x) << endl; // x�� ���밪

	return 0;
}