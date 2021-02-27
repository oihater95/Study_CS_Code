#include <iostream>
#include <string>
#include <vector>
using namespace std;

template<typename T>

vector<T> sort(vector<T>& list)
{
	for (int i = 0; i < list.size(); i++)
	{
		for (int j = 0; j < list.size()-1; j++)
		{
			T temp;
			if (list[j] > list[j + 1])
			{
				temp = list[j + 1];
				list[j + 1] = list[j];
				list[j] = temp;
			}
		}
	}

	return list;
}

template<typename T>
void print(vector<T> list)
{
	//typename T::iterator iter = list.begin();
	auto iter = list.begin();

	for (int k = 0; k < list.size(); k++)
	{
		cout << *iter << " , ";
		iter++;

	}
	cout << endl;
}


int main()
{
	vector<int> int_list(5);
	int_list = { 10,5,8,1,3 };
	vector<double> double_list(5);
	double_list = { 10.1,5.1,8.1,1.1,3.1 };
	vector<string> string_list(5);
	string_list = { "하나", "둘" , "셋" , "넷" , "다섯" };

	sort(int_list);
	sort(double_list);
	sort(string_list);

	print(int_list);
	print(double_list);
	print(string_list);

	return 0;
}