#include <iostream>
using namespace std;

class Train {
public:
	static int max;
	
	Train() {}
	Train(int people)
	{
		mPeople = people;
	}
	~Train() {}
	virtual int station(int takeOff, int takeOn)
	{
		
		mPeople -= takeOff;
		mPeople += takeOn;
		if (mPeople < 300)
		{
			return mPeople;

		}
		else
		{
			mPeople = 300;
			return mPeople;
		}
		
	}

protected:
	int mPeople; // 사람 수
};

int Train::max = 0;

class Ktx : public Train
{
public:
	Ktx() : Train(0) {}
	Ktx(int people) : Train(people)
	{
		mPeople = people;
	}
	~Ktx() {}
	// 기차에 사람이 타고 내리는 함수

	
	int station(int takeOff, int takeOn)
	{
		return Train::station(takeOff, takeOn);
	}
	
	int getPeople()
	{

		if (max > mPeople)
		{
			return max;
		}
		else
		{
			max = mPeople;
			return max;
		}
	}
};


int main()
{
	Ktx k;
	int tof=0, to=0;
	

	for (int i = 0; i < 5; i++)
	{
		cout << i+1 << "번역 : ";
		cin >> tof >> to;
		k.station(tof, to);
		k.getPeople();
		if (k.getPeople() > 300)
		{
			cout << "정원초과입니다." << endl;
			exit(100);
		}
		else if (k.getPeople()  < 0)
		{
			cout << "정원미달 입니다." << endl;
			exit(100);
		}
			

	}
	if (k.getPeople() <= 300)
	{
		cout << "가장 많은 사람이 탑승했을 때의 사람 수 = " << k.getPeople() << endl;
	}
	
	
	return 0;
}
