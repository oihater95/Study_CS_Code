#include <iostream>
#include <cmath>
using namespace std;

class Polygon
{
public:
	Polygon()
	{
		mPoint = 0, mLength = 0;
	};
	Polygon(int point, float length)
	{
		mPoint = point, mLength = length;
	}
	~Polygon() {}

	virtual void calcGirth()
	{
		if (mPoint == 0 && mLength == 0)
		{
			cout << "Girth : empty" << endl;
		}
		else if (mPoint == 0)
		{
			cout << "Girth : " << 2 * mLength * 3.14 << endl;
		}
		else
			cout << "Girth : " << mPoint * mLength << endl;

	}
	virtual void calcArea()
	{
		if (mPoint == 0 && mLength == 0)
		{
			cout << "Area : empty" << endl;
		}
		else if (mPoint == 0)
		{
			cout << "Area : " << mLength * mLength * 3.14 << endl;
		}
		else
			cout << "Area : " << mPoint * mLength * mLength / (4 * tan(3.141592 / mPoint)) << endl;
	}
protected:
	int mPoint;
	double mLength;

};

class Rectangle : public Polygon
{

public:
	Rectangle(int a, float b)
	{
		mPoint = a, mLength = b;
	}
};

class Triangle : public Polygon
{

public:
	Triangle(int a, float b)
	{
		mPoint = a, mLength = b;
	}
};

class Circle : public Polygon
{

public:
	Circle(int a, float b)
	{
		mPoint = a, mLength = b;
	}
};

int main()
{
	Triangle tri(3, 10);
	Rectangle rec(4, 10);
	Circle cir(0, 5);
	cout << "--- Triangle class ---" << endl;
	tri.calcGirth();
	tri.calcArea();
	cout << "--- Rectangle class ---" << endl;
	rec.calcGirth();
	rec.calcArea();
	cout << "--- Circle class ---" << endl;
	cir.calcGirth();
	cir.calcArea();
	return 0;
}
