#include <iostream>
#include <string>
using namespace std;

int main()
{
	int i = 0;
	string love;
	string database[] = {"���", "���α׷���", "����" ,"����ǹٺ�" ,"���뿪" , "õ���ǻ��", "�����", "��ü����"};

	cout << "Ű���� : ";
	cin >> love;
	cout << endl << "�˻���� : ";


	for (i = 0; i < 8 ; i++)
	{
		if (database[i].find(love) != -1)
		{
			cout << database[i] << " ";
		}
		

	}
			
	cout << endl;

	
	

	return 0;
}