#include <iostream>
#include <cmath>
using namespace std;

class Point
{
	
private :
	double x, y;

public:
	
	Point(double a, double b) {x=a , y=b ;};
	Point() 
	{
		x = 0, y = 0;
	};

	void setPoint(double a, double b)
	{
		x = a;
		y = b;
	}
	double getx()
	{
		return x;
	}
	double gety()
	{
		return y;
	}

	Point operator-(const Point& b)
	{
		this->x = this->x - b.x;
		this->y = this->y - b.y;
		return *this;
	}

	Point& operator = (const Point &b)
	{
		this->x = b.x;
		this->y = b.y;
		return *this;
	}

	Point operator*(const Point& b)
	{
		this->x = this->x * b.x;
		this->y = this->y * b.y;
		return Point(x, y);
	}

	ostream &operator <<(const Point& b)
	{	
		cout << b.x << " , " << b.y  << endl;
	}

	
};




int main() {
	int x1 = 0, y1 = 0, x2 = 0, y2 = 0;
	Point *pP1, *pP2, *pP3;
	cout << "ù��° ��ǥ[x1, y1]�� �Է��ϼ��� : ";
	cin >> x1 >> y1;
	cout << "�ι�° ��ǥ[x1, y1]�� �Է��ϼ��� : ";
	cin >> x2 >> y2;
	pP1 = new Point(x1, y1);
	pP2 = new Point(x2, y2);
	pP3 = new Point(); 
	*pP3 = (*pP1 - *pP2) * (*pP1 - *pP2);
	
	cout << "�� ��ǥ ������ ���̴� " << sqrt(pP3->getx() + pP3->gety()) << "�Դϴ�" << endl;;
	return 0;
}
