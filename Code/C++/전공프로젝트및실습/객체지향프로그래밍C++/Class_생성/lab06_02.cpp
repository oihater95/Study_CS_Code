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
	CStudent s[3];
	int inputNumber;
	string inputName, inputMajor;
	int length = 0;

	for (int i = 0; i < 3; i++)
		{
			cout << length + 1 << " ��° �л� �Է�" << endl;
			cout << "�й� : ";
			cin >> inputNumber;
			s[i].setNumber(inputNumber);
			cout << "�̸� : ";
			cin >> inputName;
			s[i].setName(inputName);
			cout << "���� : ";
			cin >> inputMajor;
			s[i].setMajor(inputMajor);
			if (i >= 1)
			{
				if (s[i].getNumber() == s[i - 1].getNumber())
				{
					cout << "*�ߺ��� �й��� �����մϴ�" << endl << endl;
					i--;
				}
				else
				{
					cout << "*�Է� �Ϸ�" << endl << endl;
					length++;
				}

			}
			else
			{
				length++;
				cout << "*�Է� �Ϸ�" << endl << endl;
			}

		}

	cout << "��� �Է��� �Ϸ�Ǿ����ϴ�." << endl;

	for (int j = 0; j < 3; j++)
	{
		cout << j + 1 << "�л�����" << endl;
		cout << "�й� : " << s[j].getNumber() << endl;
		cout << "�̸� : " << s[j].getName() << endl;
		cout << "���� :" << s[j].getMajor() << endl << endl;
		
	}


	return 0;
}