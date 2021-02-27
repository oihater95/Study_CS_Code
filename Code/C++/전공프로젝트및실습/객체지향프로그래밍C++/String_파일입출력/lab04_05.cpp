#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	string line;
	int length;
	ofstream text, fout;
	char ch;
	ifstream fin;
	text.open("Text.txt");
	text << "In this paper, we explore the feasibility of a" << endl << "medical training system for breast tumor palpation based on haptic" << endl
		<< "augmented reality (AR) technology. Haptic AR is an emerging" << endl
		<< "research area in haptics and virtual reality" << endl
		<< "(VR), which is concerned" << endl
		<< "with augmenting the haptic" << endl
		<< "properties of a real object by means of virtual haptic" << endl
		<< "feedback. The AR-based tumor palpation system" << endl
		<< "consists of a real breast sample.";
		

	text.close();

	cout << "length = ";
	cin >> length;
	fin.open("Text.txt");
	fout.open("output.txt");
	int count = 0;
	while(fin.is_open())
	{ 
		for (int i = 0; i < length; i++)
		{
			fin.get(ch);
			if (ch == '.')
			{
				fout << ch;
				cout << ch;
				count+=1;
				if (count == 2)
				{
					
					fin.close();
					break;
				}
				else
					continue;
			}
			else if (ch == '\n')
			{
				i--;
				count = 0;
			}
			else
			{
				count = 0;
				fout << ch;
				cout << ch;
			}
		}
		fout << endl;
		cout << endl;
		
	}
	
	fout.close();
	return 0;
}