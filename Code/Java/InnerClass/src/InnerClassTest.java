class Outside { // 외부 클래스 , top level 클래스
	public class Inside { // 내부 ㅡㄹ래스를 일반 멤버 변수와 동일한 위치에 정의
		
	}
	
	public static class StaticInner {
		
	}
}

class Animal {
	void performBehavior() { 
		//이름이 있는 지역 내부 클래스, 컴파일 시 Animal$1$Brain.class생성
		class Brain {
			
		}
	}
}
public class InnerClassTest {

	public static void main(String[] args) {
		Outside.StaticInner sinner = new Outside.StaticInner(); // static 내부 클래스는 외부 클래스 객체 생성없이 객체생성가능 
		Outside outer = new Outside();
		Outside.Inside inner = outer.new Inside();
	}

}
// 컴파일 시
// 외부 클래스 Outside.class / 내부 클래스 Outside$Inside.class 생성
