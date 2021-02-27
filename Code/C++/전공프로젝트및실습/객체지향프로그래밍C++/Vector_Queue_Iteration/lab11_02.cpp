#include <iostream>
#include <string>
#include <functional>
#include <vector>
using namespace std;

char* reverse(string input)
{
	char *temp = new char[input.size() + 1];

	auto ch = input.rbegin();

	for (int i = 0; i < input.size(); i++) {
		temp[i] = *ch;
		ch++;
	}
	temp[input.size() + 1] = '\0';

	return temp;
}

/* 12345
       5�� end�� �ƴϰ� 5������ end   rbegin�� ��������
*/

int main()
{
	string input;
	auto iter = input.begin();
	while (1)
	{
		cout << "���ڿ� �ϳ��� �Է����ּ��� : ";
		cin >> input;
		cout << "�Է��Ͻ� ���ڿ��� ���� : ";
		char* reverseString = reverse(input);
		cout << reverseString << endl;

		int count = 0;

		for (int a = 0; a < input.size(); a++)
		{
			if (*iter != reverseString[a])
			{
				count++;

			}
			

		}

		if (count == 0)
		{
			cout << "�� ���ڴ� ȸ���Դϴ�." << endl;
		}

		else
		{
			cout << "�� ���ڴ� ȸ���� �ƴմϴ�." << endl;
		}
		cout << endl;

		if (input == "��")
		{
			break;
		}

	}

	
	

	return 0;
}