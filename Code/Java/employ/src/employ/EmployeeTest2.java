package employ;
// static을 사용(클래스변수)해 메모리 낭비 피하기

// Employee 클래스 선언
class Employee3 {
	String name;
	int employeeNo;
	int age;
	static String companyName = "S전자"; // 동일한 값 갖는 변수 (클래스 변수)
	//-> 인스턴스 변수가 아닌 클래스 변수로 선언하는 것이 메모리상 유리
}

// Employee 클래스 객체 생성 및 값 할당
public class EmployeeTest2  {
	public static void main(String[] args) {
		Employee3 kim = new Employee3();
		kim.name = "김종진";
		kim.employeeNo = 12345;
		kim.age = 45;
		
		Employee3 lee = new Employee3();
		lee.name = "이선영";
		lee.employeeNo = 12346;
		lee.age = 39;
		
		Employee3 park = new Employee3();
		park.name = "박재성";
		park.employeeNo = 12347;
		park.age = 28;
		
		// 클래스 변수 값 변경
		// companyName = s전자, 출력 : s전자
		System.out.println("kim의 회사명 : " + kim.companyName);
		
		// companyName = a전자 로 변경, 출력 : a전자
		lee.companyName = "A전자";
		System.out.println("lee의 회사명 : " + kim.companyName);
		
		// lee 참조 변수에 의해 a전자로 변경됨, 출력 : a전자
		System.out.println("park의 회사명 : " + kim.companyName);
	}

}
