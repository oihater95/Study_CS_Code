#include <iostream>
#include <cmath>
using namespace std;

template <typename type>

class Point
{
private:
	type x1;
	type x2;
	type y1;
	type y2;

public :
	Point<type>() {};

	void setPointFromKeyboard()
	{
		cout << "첫번째 x : ";
		cin >> x1;
		cout << "첫번째y : ";
		cin >> y1;
		cout << "두번째 x : ";
		cin >> x2;
		cout << "두번째 y : ";
		cin >> y2;
		cout << endl;

	}

	type print()
	{
		cout << "두점 사이의 거리 = ";
		return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
	}

};


int main()
{
	Point<int> p;

	p.setPointFromKeyboard();

	cout << p.print();
	cout << endl;

	Point<double> p2;
	p2.setPointFromKeyboard();
	cout << p2.print() << endl;


	return 0;
}