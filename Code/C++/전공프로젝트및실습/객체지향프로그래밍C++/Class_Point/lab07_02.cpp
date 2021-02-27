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
	cout << "첫번째 좌표[x1, y1]를 입력하세요 : ";
	cin >> x1 >> y1;
	cout << "두번째 좌표[x1, y1]를 입력하세요 : ";
	cin >> x2 >> y2;
	pP1 = new Point(x1, y1);
	pP2 = new Point(x2, y2);
	pP3 = new Point(); 
	*pP3 = (*pP1 - *pP2) * (*pP1 - *pP2);
	
	cout << "두 좌표 사이의 길이는 " << sqrt(pP3->getx() + pP3->gety()) << "입니다" << endl;;
	return 0;
}
