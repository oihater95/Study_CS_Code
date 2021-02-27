#include <iostream>
#include <string>
#include <ctime>
using namespace std;

class Avengers 
{
	public:  
		Avengers() 
		{ 
			name = "";   
			attack_point = 0;   
			defense_point = 0;  
			health = 100; 
		}
		~Avengers() {}  //캐릭터 설정 함수 
		virtual void set(string _name, int _attack, int _defense, int _health)  
		{
			name = _name;
			attack_point = _attack;
			defense_point = _defense;
			health = _health;
		} 
		virtual int attack()  //공격 함수  
		{

			return attack_point; 
		} 
		virtual void defense(int _attack_point)  //방어 함수  
		{
			if (health > (_attack_point-defense_point))
			{
				
				health = health - (_attack_point-defense_point);
			}
			else if (health <= (_attack_point-defense_point))
			{
				health = 0;
			}
		} 
		virtual void print_info()   //캐릭터 정보 출력 함수 
		{
			
			cout << "Name : " << name << endl;
			cout << "Attack_Point : " << attack_point << endl;
			cout << "Defense_Point : " << defense_point << endl;
			cout << "Health : " << health << endl;
		}
	protected: 
		string name;//캐릭터 이름  
		int attack_point;//공격력  
		int defense_point;//방어력 
		int health;//체력
}; 

class Character : public Avengers
{
		public:  

			Character() : Avengers() {}
			~Character() {}

			int get_health()
			{
				return health;
			}

			void set(string _name, int _attack_point, int _defense_point, int _health)
			{
				Avengers::set(_name, _attack_point, _defense_point, _health);
			}

			int attack()
			{
				return Avengers::attack();
			}

			void defense(int _attack_point)
			{
				Avengers::defense(_attack_point);
			}
			void print_info()
			{
				Avengers::print_info();
			}

			

}; 

int main() 
{
	Character my_char;  
	Character enemy_char;  
	string hero;
	cout << "Choose your character(IronMan, CaptainAmerica, Thor) : ";
	cin >> hero;

	if (hero == "IronMan")
	{
		my_char.set("IronMan", 70, 40, 100);
	}
	else if (hero == "CaptainAmerica")
	{
		my_char.set("CaptainAmerica", 60, 50, 100);
	}
	else if (hero == "Thor")
	{
		my_char.set("Thor", 80, 30, 100);
	}

	srand((unsigned int)time(NULL));
	switch (rand() % 3 + 1)
	{
	case 1:
		enemy_char.set("IronMan", 70, 40, 100);
		break;

	case 2:
		enemy_char.set("CaptainAmerica", 60, 50, 100);
		break;

	case 3:
		enemy_char.set("Thor", 80, 30, 100);
		break;
	}
	cout << "--" << "My Character" << "--" << endl;
	my_char.print_info();
	cout << "--" << "Enemy Character" << "--" << endl;
	enemy_char.print_info();
	cout << endl;

	cout << endl << "--Battle--" << endl;  
	cout << "My Life: " << my_char.get_health() << "\t" << "Enemy Life:" << enemy_char.get_health() << endl;

	while (1)
	{   
		enemy_char.defense(my_char.attack());
		cout << "My Life : " << my_char.get_health() << "\t" << "Enemy Life:" << enemy_char.get_health() << endl;
		if (enemy_char.get_health() == 0)
		{
			cout << "You Win!" << endl;
			break;
		}
		my_char.defense(enemy_char.attack());
		cout << "My Life : " << my_char.get_health() << "\t" << "Enemy Life:" << enemy_char.get_health() << endl;

		if (my_char.get_health() == 0)
		{
			cout << "You Lose..." << endl;
			break;
		}
	} 
	
	return 0;
}