#include <iostream>
#include <string>
#include <vector>
using namespace std;

class CStudent
{
private:
	string Major;
	string Name;
	int Number;


public:
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
	CStudent s[3];
	int inputNumber;
	string inputName, inputMajor;
	int length = 0;

	for (int i = 0; i < 3; i++)
		{
			cout << length + 1 << " 번째 학생 입력" << endl;
			cout << "학번 : ";
			cin >> inputNumber;
			s[i].setNumber(inputNumber);
			cout << "이름 : ";
			cin >> inputName;
			s[i].setName(inputName);
			cout << "전공 : ";
			cin >> inputMajor;
			s[i].setMajor(inputMajor);
			if (i >= 1)
			{
				if (s[i].getNumber() == s[i - 1].getNumber())
				{
					cout << "*중복된 학번이 존재합니다" << endl << endl;
					i--;
				}
				else
				{
					cout << "*입력 완료" << endl << endl;
					length++;
				}

			}
			else
			{
				length++;
				cout << "*입력 완료" << endl << endl;
			}

		}

	cout << "모든 입력이 완료되었습니다." << endl;

	for (int j = 0; j < 3; j++)
	{
		cout << j + 1 << "학생정보" << endl;
		cout << "학번 : " << s[j].getNumber() << endl;
		cout << "이름 : " << s[j].getName() << endl;
		cout << "전공 :" << s[j].getMajor() << endl << endl;
		
	}


	return 0;
}