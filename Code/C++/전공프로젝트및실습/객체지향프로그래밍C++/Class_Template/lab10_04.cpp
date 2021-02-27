#include <iostream>
#include <list>
using namespace std;

template <typename T>
class CList
{
public:
	CList()
	{
		m_Length = 0;
		m_Array[5] = {};

	}
	~CList() {};

	bool IsEmpty()
	{
		if (m_Length == 0)
		{
			return true;
		}
		else
			return false;

	}
	// list가 비어 있으면 1, 아니면 0  
	bool IsFull()
	{
		if (m_Length == 5)
			return true;
		else
			return false;
	}// list가 꽉 차 있으면 1, 아니면 0 

	void Add(T data)
	{

		if (IsFull() == 1)
		{
			cout << "List is full." << endl;
		}
		else
		{
			
			int temp;
			if (m_Length != 0)
			{
				for (int k = 0; k < m_Length; k++)
				{
					if (m_Array[k] == data)
					{
						cout << "중복된 데이터가 존재" << endl;
						m_Length--;
						break;
					}

					else
					{
						m_Array[m_Length] = data;
						for (int l = m_Length; l > 0 ; l--)
						{
							if (m_Array[l] < m_Array[l-1])
							{
								temp = m_Array[l-1];
								m_Array[l-1] = m_Array[l];
								m_Array[l] = temp;
							}
						}
					}

				}

				

			}
			else
			{
				m_Array[m_Length] = data;

			}
		
			m_Length++;
		}
	}// list에 데이터 추가 


	void Delete(T data)
	{
		if (IsEmpty() == 1)
		{
			cout << "List is Empty." << endl;
		}
		else
		{
			int index = -1;
			for (int i = 0; i < 4; i++)
			{
				if (m_Array[i] == data)
				{
					index = i;
					break;

				}

			}
			if (index == -1)
			{
				cout << "Data is not found." << endl;
			}
			else
			{
				for (int a = index; a < 4 - index; a++)
				{
					m_Array[a] = m_Array[a + 1];
				}
				m_Length--;
			}

		}
	}// list에 데이터 삭제 
	void Print()
	{
		cout << "* Current List" << endl;
		for (int j = 0; j < m_Length; j++)
		{

			cout << m_Array[j] << " ";
		}
		cout << endl;
	}// list에 데이터 출력 

private:
	T m_Array[5]; // 데이터를 저장할 공간  
	int m_Length; // list에 있는 데이터 수 

};

int command()
{
	int num;
	cout << "\n\t---- menu ----" << endl;
	cout << "\t1. 리스트 추가" << endl;
	cout << "\t2. 리스트 삭제" << endl;
	cout << "\t3. 리스트 출력" << endl;
	cout << "\t4. 프로그램 종료" << endl;
	cout << "\n\t입력 -->";
	cin >> num;

	return num;
}

int main()
{
	CList<int> list;
	int input;
	int com;

	while (1)
	{
		com = command();

		switch (com)
		{
		case 1:
			cout << "\n추가할 데이터 : ";
			cin >> input;
			list.Add(input);
			break;

		case 2:
			cout << "\n삭제할 데이터 : ";
			cin >> input;
			list.Delete(input);
			break;

		case 3:
			list.Print();
			break;

		case 4:
			cout << "\n\t프로그램을 종료합니다 \n" << endl;
			return 0;
			break;

		default:
			break;
		}
	}

	return 0;
}