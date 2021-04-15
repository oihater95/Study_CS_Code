package employ;
// 인스턴스 변수에 의한 메모리 낭비 예제

// Employee 클래스 선언
class Employee2 {
	String name;
	int employeeNo;
	int age;
	String companyName; // 동일한 값 갖는 변수 
	//-> 인스턴스 변수가 아닌 클래스 변수로 선언하는 것이 메모리상 유리
}

// Employee 클래스 객체 생성 및 값 할당
public class EmployeeTest {
	public static void main(String[] args) {
		Employee2 kim = new Employee2();
		kim.name = "김종진";
		kim.employeeNo = 12345;
		kim.age = 45;
		kim.companyName = "S전자";
		
		Employee2 lee = new Employee2();
		lee.name = "이선영";
		lee.employeeNo = 12346;
		lee.age = 39;
		lee.companyName = "S전자";
		
		Employee2 park = new Employee2();
		park.name = "박재성";
		park.employeeNo = 12347;
		park.age = 28;
		park.companyName = "S전자";

	}

}
