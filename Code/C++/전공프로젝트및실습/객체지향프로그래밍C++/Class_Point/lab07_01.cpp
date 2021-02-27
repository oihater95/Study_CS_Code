#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

class User
{
private :
	string name;
	int pw;

public:
	User(string _name, int _pw)
	{
		name = _name;
		pw = _pw;
	}
	User()
	{
	}

	void setid(string _name)
	{
		name = _name;
	}
	void setpw(int _pw)
	{
		pw = _pw;
	}

	string getid()
	{
		return name;
	}

	int getpw()
	{
		return pw;
	}

};



int main()
{
	User user[3];
	string id, searchId;
	int password, searchPassword, count1 = 0;

	for (int i = 0; i < 3; i++)
	{
		cout << setw(12) << setfill('=') << " " << i + 1 << " ============" << endl;
		cout << "Id : ";
		cin >> id;
		user[i].setid(id);
		if (i == 1)
		{
			if (user[i].getid() == user[i - 1].getid())
			{
				cout << "이미 존재하는 ID입니다." << endl;
				count1 = 1;
				break;
			}
		}
		else if (i == 2)
		{
			if (user[i].getid() == user[i - 1].getid())
			{
				cout << "이미 존재하는 ID입니다." << endl;
				count1 = 1;
				break;
			}
			else if(user[i].getid() == user[i - 2].getid())
			{
				cout << "이미 존재하는 ID입니다." << endl;
				count1 = 1;
				break;
			}
		}
		if (count1 == 1)
		{
			cout << "종료합니다" << endl;
			
		}
		cout << "passoword : ";
		cin >> password;
		user[i].setpw(password);
		cout << "==========================" << endl << endl;

		
		
	}

	while (1)
	{
		if (count1 == 1)
		{
			break;
		}

		cout << setw(12) << setfill('=') << " Log In " << "============" << endl<< endl;
		cout << "Id : ";
		cin >> searchId;
		
		
		if (user[0].getid() == searchId)
		{
			cout << "Password : ";
			cin >> searchPassword;
			if (user[0].getpw() == searchPassword)
			{
				cout << "로그인 되셨습니다." << endl << "=======================" << endl << endl;
			}
			else
			{
				cout << "잘못된 ID거나 PASSWORD 입니다." << endl << "=======================" << endl << endl;
			}
		}
		else if(user[1].getid() == searchId)
		{
			cout << "Password : ";
			cin >> searchPassword;
			if (user[1].getpw() == searchPassword)
			{
				cout << "로그인 되셨습니다." << endl << "=======================" << endl << endl;
			}
			else
			{
				cout << "잘못된 ID거나 PASSWORD 입니다." << endl << "=======================" << endl << endl;
			}
		}
		else if (user[2].getid() == searchId)
		{
			cout << "Password : ";
			cin >> searchPassword;
			if (user[2].getpw() == searchPassword)
			{
				cout << "로그인 되셨습니다." << endl << "=======================" << endl << endl;
			}
			else
			{
				cout << "잘못된 ID거나 PASSWORD 입니다." << endl << "=======================" << endl << endl;
			}
		}
		else
			cout << "잘못된 ID거나 PASSWORD 입니다." << endl << "=======================" << endl << endl;

		if (searchId == "종료")
		{
			cout << "종료합니다." << endl;
			break;
		}
		

	}
	return 0;
}