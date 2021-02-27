#include <iostream>
#include <cmath>
using namespace std;

class Polygon
{
public :
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
		else
		cout << "Girth : " << mPoint * mLength << endl;
		
	}
	virtual void calcArea()
	{
		if (mPoint == 0 && mLength == 0)
		{
			cout << "Area : empty" << endl;
		}
		else
		cout << "Area : " << mPoint * mLength * mLength /( 4 * tan(3.141592 / mPoint))   << endl;
	}
protected:
	int mPoint;
	double mLength;
	
};

class Rectangle : public Polygon
{

public :
	Rectangle(int a, float b)
	{
		mPoint = a, mLength = b;
	}
};



int main()
{
	Polygon pol;
	Rectangle rec(4, 10);
	cout << "--- Polygon class ---" << endl;
	pol.calcGirth();
	pol.calcArea();
	cout << "--- Rectangle class ---" << endl;
	rec.calcGirth();
	rec.calcArea();
	return 0;
}

