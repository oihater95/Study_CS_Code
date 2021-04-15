class Employee {
	String name;
	int deptNo;
	String grade;
}

class Manager extends Employee {
	String boss;
	char grade; // 자식 클래스에서 재정의 -> char형으로 변환
	void printGrade() {
		this.grade = 'A'; // 자식클래스에서 재정의하여 this.grade = char형
		super.grade = "A등급"; // 부모클래스의 grade를 참조했기 때문에 super.grade = string
		System.out.println("자식 객체의 grade : " + this.grade);		
		System.out.println("부모 객체의 grade : " + super.grade);
	}
}
public class Employee_super {

	public static void main(String[] args) {
		Manager kim = new Manager();
		kim.printGrade();

	}

}
