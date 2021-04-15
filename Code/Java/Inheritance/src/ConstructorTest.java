class SuperClass {
	int num1;
	public SuperClass() { // 부모클래스 생성자 호출시 num1=100초기화, 매개변수없는 기본생성자
		System.out.println("SuperClass 객체 생성");
		num1 = 100;
	}
}

class SubClass extends SuperClass {
	int num2;
	public SubClass() { // 자식클래스 생성자 호출시 num2=10000초기화
		System.out.println("SubClass 객체 생성");
		num2 = 10000;
	}
}
public class ConstructorTest {

	public static void main(String[] args) {
		SubClass sub = new SubClass(); // 자식클래스 객체 생성하여 변수 값 출력
		System.out.println(sub.num1);
		System.out.println(sub.num2); 
		/* 부모 클래스 객체가 생성되기 위해서는 부모 클래스 생성자가 호출되어야함
		 * 자식 클래스에는 어디에도 부모 클래스 생성자는 없음, 부모클래스의 기본생성자가 자동으로 호출됨
		 * 부모 클래스에 기본 생성자 없는 경우 에러발생*/
		 
	}

}
