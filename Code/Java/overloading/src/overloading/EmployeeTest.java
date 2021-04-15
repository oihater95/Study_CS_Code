package overloading;
class Employee {
	String name;
	int age;
	int salary;
	// �޼��� overloading

	void setEmployee(String name) {
		this.name = name;
	}
	
	void setEmployee(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	void setEmployee() {
		name = "No name";
		age = 0;
	}
	
	// ������ overloading
	public Employee() { // �⺻ ������
	}
	
	public Employee(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	public Employee(String name, int age, int salary) {
		this(name, age); // ���� ������ �ߺ��Ǵ� �κ� this()ó��
		this.salary = salary;
	}
}
public class EmployeeTest {

	public static void main(String[] args) {
		Employee park = new Employee();
		park.setEmployee("���缺", 28);
		Employee lee = new Employee("���缺", 30);
		System.out.println(park.name + lee.age);
	}

}