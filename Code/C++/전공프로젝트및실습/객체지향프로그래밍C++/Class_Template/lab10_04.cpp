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
	// list�� ��� ������ 1, �ƴϸ� 0  
	bool IsFull()
	{
		if (m_Length == 5)
			return true;
		else
			return false;
	}// list�� �� �� ������ 1, �ƴϸ� 0 

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
						cout << "�ߺ��� �����Ͱ� ����" << endl;
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
	}// list�� ������ �߰� 


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
	}// list�� ������ ���� 
	void Print()
	{
		cout << "* Current List" << endl;
		for (int j = 0; j < m_Length; j++)
		{

			cout << m_Array[j] << " ";
		}
		cout << endl;
	}// list�� ������ ��� 

private:
	T m_Array[5]; // �����͸� ������ ����  
	int m_Length; // list�� �ִ� ������ �� 

};

int command()
{
	int num;
	cout << "\n\t---- menu ----" << endl;
	cout << "\t1. ����Ʈ �߰�" << endl;
	cout << "\t2. ����Ʈ ����" << endl;
	cout << "\t3. ����Ʈ ���" << endl;
	cout << "\t4. ���α׷� ����" << endl;
	cout << "\n\t�Է� -->";
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
			cout << "\n�߰��� ������ : ";
			cin >> input;
			list.Add(input);
			break;

		case 2:
			cout << "\n������ ������ : ";
			cin >> input;
			list.Delete(input);
			break;

		case 3:
			list.Print();
			break;

		case 4:
			cout << "\n\t���α׷��� �����մϴ� \n" << endl;
			return 0;
			break;

		default:
			break;
		}
	}

	return 0;
}