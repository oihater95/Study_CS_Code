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
		Name = "ȫ�浿";
		Major = "��ǻ�Ͱ��а�";
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
		cout << "�й� : " << Number << endl << "�̸� : " << Name << endl << "���� : " << Major << endl << endl;
	}
};

int main()
{
	CStudent s1;
	s1.Display();

	CStudent s2(1999000000, "����ö", "���ؿ�ȭ��");
	s2.Display();

	s1.setNumber(2006000000);
	s1.setName("�ΰ���");
	s1.setMajor("����Ʈ���");
	cout << "�й� : " << s1.getNumber() << endl;
	cout << "�̸� : " << s1.getName() << endl;
	cout << "���� : " << s1.getMajor() << endl;

	return 0;
}