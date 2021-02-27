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
       5가 end가 아니고 5다음이 end   rbegin도 마찬가지
*/

int main()
{
	string input;
	auto iter = input.begin();
	while (1)
	{
		cout << "문자열 하나를 입력해주세요 : ";
		cin >> input;
		cout << "입력하신 문자열의 역순 : ";
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
			cout << "이 문자는 회문입니다." << endl;
		}

		else
		{
			cout << "이 문자는 회문이 아닙니다." << endl;
		}
		cout << endl;

		if (input == "끝")
		{
			break;
		}

	}

	
	

	return 0;
}