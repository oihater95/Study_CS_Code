class Employee {
	String name;
	int deptNo;
	String grade;
}

class Manager extends Employee {
	String boss;
	char grade; // �ڽ� Ŭ�������� ������ -> char������ ��ȯ
	void printGrade() {
		this.grade = 'A'; // �ڽ�Ŭ�������� �������Ͽ� this.grade = char��
		super.grade = "A���"; // �θ�Ŭ������ grade�� �����߱� ������ super.grade = string
		System.out.println("�ڽ� ��ü�� grade : " + this.grade);		
		System.out.println("�θ� ��ü�� grade : " + super.grade);
	}
}
public class Employee_super {

	public static void main(String[] args) {
		Manager kim = new Manager();
		kim.printGrade();

	}

}
