package finalModifier;

//static을 사용(클래스변수)해 메모리 낭비 피하기
//Employee 클래스 선언
class Employee4 {
	String name;
	int employeeNo;
	int age;
	final static String COMPANY_NAME = "S전자"; // 동일한 값 갖는 변수 (클래스 변수)
	//-> 인스턴스 변수가 아닌 클래스 변수로 선언하는 것이 메모리상 유리
	// final 예약어로 선언하여 상수 취급(변경 불가)
}

//Employee 클래스 객체 생성 및 값 할당
public class EmployeeTest_final_static  {
	public static void main(String[] args) {
		System.out.println("직원들의 회사명 : " + Employee4.COMPANY_NAME);
		Employee4.COMPANY_NAME = "A전자" // final 변수 변경 시 에러
	}

}