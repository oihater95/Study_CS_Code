#include <iostream>
#include <vector>
#include <exception>
#include <fstream>
#include <string>
using namespace std;

class CStudent
{
private:
	string m_Name;
	int m_Number;
	string m_Major;

public:
	CStudent(string _Name, int _Number, string _Major)
	{
		m_Number = _Number;
		m_Name = _Name;
		m_Major = _Major;
	}

	CStudent()
	{
		m_Number = 2018000000;
		m_Name = "ȫ�浿";
		m_Major = "��ǻ�Ͱ��а�";
	}

	~CStudent(){}

	void setName(string n)
	{
		m_Name = n;
	}
	
	string getName()
	{
		return m_Name;
	}

	void setNumber(int n)
	{
		m_Number = n;
	}

	int getNumber()
	{
		return m_Number;
	}

	void setMajor(string n)
	{
		m_Major = n;
	}

	string getMajor()
	{
		return m_Major;
	}

	void setAll(string name, int number, string major)
	{
		m_Name = name;
		m_Number = number;
		m_Major = major;
	}

	void Display()
	{
		cout << "�̸� : " << m_Name << "\n";
		cout << "�й� : " << m_Number << "\n";
		cout << "���� : " << m_Major << "\n\n";
	}

};


class FileNotFounException : public exception
{
	string message;
public:
	FileNotFounException(const string& fname) : message("File \"" + fname + "\" not found"){}

	virtual const char* what() const throw()
	{
		return message.c_str();
	}
};

vector<CStudent> read_file(string &filename) // ������ �Լ��ϻ� ���ʹ� �ƴϴ�.
{
	vector<CStudent> vec;
	ifstream fin;
	try {
		if (filename != "data.txt")
			throw FileNotFounException(filename);
		fin.open(filename);
	}
	catch (FileNotFounException& e) {
		cout << e.what() << endl;
		return vec;
	}

	fin.open(filename);
	string strtxt1, strtxt2;
	int numtxt;

	CStudent s1;
	fin >> strtxt1;
	fin >> numtxt;
	fin >> strtxt2;
	s1.setAll(strtxt1, numtxt, strtxt2);

	vec.push_back(s1);

	CStudent s2;
	fin >> strtxt1;
	fin >> numtxt;
	fin >> strtxt2;
	s2.setAll(strtxt1, numtxt, strtxt2);

	vec.push_back(s2);

	CStudent s3;
	fin >> strtxt1;
	fin >> numtxt;
	fin >> strtxt2;
	s3.setAll(strtxt1, numtxt, strtxt2);

	vec.push_back(s3);

	return vec;
}


int main()
{
	string str;

	cout << "���� �̸� : ";
	cin >> str;
	

	try
	{
		vector<CStudent> numbers = read_file(str);
		for (CStudent value : numbers)
		{
			value.Display();
		}
	}
	catch (exception& e)
	{
		cout << e.what() << '\n';
	}

	return 0;
}