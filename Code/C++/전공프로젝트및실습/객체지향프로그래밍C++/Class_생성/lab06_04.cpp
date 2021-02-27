#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

class Student
{
private:
	string name;
	int id;
	string major;
	vector<string> list;
	vector<char> grade;

public:
	Student(string std_name, int std_id, string std_major)
	{
		name = std_name;
		id = std_id;
		major = std_major;
	}
	Student() {}

	string getName()
	{
		return name;
	}

	int getID()
	{
		return id;
	}

	string getdept()
	{
		return major;
	}

	void setName(string std_name)
	{
		name = std_name;
	}

	void setID(int std_id)
	{
		id = std_id;
	}

	void setdept(string std_major)
	{
		major = std_major;
	}

	void print()
	{
		cout << name << " " << id << " " << major;

	}

	void addGrade(string subject, char score)
	{
		list.push_back(subject);
		grade.push_back(score);

	}

	void printGrades()
	{
		for (unsigned int i = 0; i<list.size(); i++)
			cout << list[i] << " " << grade[i] << endl;
	}

	float getGPA()
	{

		float sum = 0;
		float avr;

		for (unsigned int i = 0; i<grade.size(); i++)
		{
			if (grade[i] == 'A')
				sum += 4;
			else if (grade[i] == 'B')
				sum += 3;
			else if (grade[i] == 'C')
				sum += 2;
			else if (grade[i] == 'D')
				sum += 1;
			else if (grade[i] == 'F')
				sum += 0;
			else
				break;
		}

		int size = grade.size();
		avr = sum / (float)size;
		return avr;

	}



	void getYear(int year) {

		if (year - (id / 1000000) == 0)
			cout << "Freshmen(1학년)" << endl;
		else if (year -(id / 1000000)  == 1)
			cout << "Sophomore(2학년)" << endl;
		else if (year - (id / 1000000) == 2)
			cout << "Junior(3학년)" << endl;
		else if (year - (id / 1000000) == 3)
			cout << "Senior(4학년)" << endl;
		else
			cout << "About to graduate(5학년 이상)" << endl;
	}


};

int main() {
	Student harry("Harry", 2017310973, "CS");
	harry.print();
	cout << endl;
	harry.getYear(2019);
	harry.addGrade("Programming", 'A');
	harry.addGrade("Basic Circuit", 'B');
	harry.printGrades();
	cout << "GPA : " << harry.getGPA() << endl;
	cout << endl;

	Student ron;
	ron.setName("Ron");
	ron.setID(2014108888);
	ron.setdept("EE");
	ron.print();
	cout << endl;
	ron.getYear(2019);
	ron.addGrade("Computer Architecture", 'B');
	ron.addGrade("Maching Learning", 'B');
	ron.addGrade("Computer Vision", 'C');
	ron.printGrades();
	cout << "GPA : " << ron.getGPA() << endl;


}
