#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ofstream docu1, docu2,fout;

	docu1.open("docu1.txt");
	docu2.open("docu2.txt");
	

	docu1 << "On its 60th anniversary in 2009, Kyung" << endl << "Hee University prepared for a second leap" << endl << "forward while seeking a new paradigm of future" << endl << "university development.";
	docu2 << "In this paper, we explore the feasibility of a" << endl << "medical training system for breast tumor palpation" << endl << "based on haptic augmented reality (AR) technology. ";

	cout <<  "On its 60th anniversary in 2009, Kyung" << endl << "Hee University prepared for a second leap" << endl << "forward while seeking a new paradigm of future" << endl << "university development." << endl;
	cout << "In this paper, we explore the feasibility of a" << endl << "medical training system for breast tumor palpation" << endl << "based on haptic augmented reality (AR) technology. " << endl;

	docu1.close();
	docu2.close();

	ifstream fin;
	string line;
	fin.open("docu1.txt");
	fout.open("result.txt");
	while (getline(fin, line))
	{
		fout << line << endl;
		cout << line << endl;
	}

	fin.close();
	fout << endl;
	cout << endl;
	fin.open("docu2.txt");

	while (getline(fin, line))
	{
		cout << line << endl;
		fout << line << endl;
	}
	fin.close();
	fout.close();
	return 0;
}