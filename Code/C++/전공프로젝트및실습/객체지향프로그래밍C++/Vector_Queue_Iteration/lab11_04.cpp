#include <iostream>
#include <list>
using namespace std;

template <typename T>

class Queue
{
private :
	T* p_list;
	int size=0;
	int MAX_SIZE ;

public:

	Queue(int _MAX_SIZE = 1000)
	{
		p_list = new T[_MAX_SIZE];
	}
	~Queue() {};

	int find_index(T _item)
	{
		
	
			for (int i = 0; i < size; i++)
			{
				if (p_list[i] == _item)
				{
					return i;
				}
				
					

			}
		
			return -1;
	}

	void Enqueue(T _item)
	{
		if (size == 0)
		{
			p_list[0] = _item;
			size++;
		}
		else
		{
			if (find_index(_item) == -1)
			{
				if (size < 1000)
				{
					p_list[size] = _item;
					size++;

				}
			}
			

			
		}

		
		

	}

	T Dequeue()
	{
		T temp = 0;
		if (size != 0)
		{
			temp = p_list[0];
			for (int j = 0; j < size-1; j++)
			{
				p_list[j] = p_list[j + 1];
			}
			size--;
		}
		return temp;
	}

	void print()
	{
		cout << "Items in the list : ";
		for (int a = 0; a < size; a++)
		{
			cout << p_list[a] << " , ";

		}
		cout << endl;

	}

	int get_size()
	{
		return size;

	}

	T get_item(int _index)
	{
		return p_list[_index];

	}

};








int main()
{
	Queue<int> int_queue;
	Queue<float> float_queue;
	Queue<char> char_queue;

	int_queue.Enqueue(1);
	int_queue.Enqueue(2);
	int_queue.Enqueue(2);
	int_queue.Enqueue(5);

	float_queue.Enqueue(4.3);
	float_queue.Enqueue(2.5);
	float_queue.Enqueue(3.7);
	float_queue.Enqueue(3.7);

	char_queue.Enqueue('b');
	char_queue.Enqueue('b');
	char_queue.Enqueue('c');
	char_queue.Enqueue('a');

	cout << "<Before Dequeue>" << endl;

	int_queue.print();
	float_queue.print();
	char_queue.print();

	int_queue.Dequeue();
	float_queue.Dequeue();
	float_queue.Dequeue();
	char_queue.Dequeue();
	char_queue.Dequeue();
	char_queue.Dequeue();
	char_queue.Dequeue();

	cout << "<After Dequeue>" << endl;

	int_queue.print();
	float_queue.print();
	char_queue.print();

	return 0;
}