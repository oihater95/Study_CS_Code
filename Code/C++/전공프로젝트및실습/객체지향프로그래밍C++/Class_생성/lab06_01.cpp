#include <iostream>
#include <string>
using namespace std;

class CStudent
{
private :
	string Major;
	string Name;
	int Number;


public :
	CStudent(int _Number, string _Name, string _Major)
	{
		Number = _Number;
		Name = _Name;
		Major = _Major;

	}
	CStudent() 
	{
		Number = 2018000000;
		Name = "홍길동";
		Major = "컴퓨터공학과";
	}

	void setNumber(int _Number)
	{
		Number = _Number;
	}

	void setName(string _Name)
	{
		Name = _Name;
	}

	void setMajor(string _Major)
	{
		Major = _Major;
	}

	int getNumber()
	{
		return Number;
	}

	string getName()
	{
		return Name;
	}

	string getMajor()
	{
		return Major;
	}

	void Display()
	{
		cout << "학번 : " << Number << endl << "이름 : " << Name << endl << "전공 : " << Major << endl << endl;
	}
};

int main()
{
	CStudent s1;
	s1.Display();

	CStudent s2(1999000000, "공지철", "연극영화과");
	s2.Display();

	s1.setNumber(2006000000);
	s1.setName("민경훈");
	s1.setMajor("포스트모던");
	cout << "학번 : " << s1.getNumber() << endl;
	cout << "이름 : " << s1.getName() << endl;
	cout << "전공 : " << s1.getMajor() << endl;

	return 0;
}