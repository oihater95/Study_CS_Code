#include <iostream>
#include <string>
using namespace std;

int main()
{
	int i = 0;
	string love;
	string database[] = {"사랑", "프로그래밍", "의자" ,"사랑의바보" ,"영통역" , "천년의사랑", "냉장고", "객체지향"};

	cout << "키워드 : ";
	cin >> love;
	cout << endl << "검색결과 : ";


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