package abstractModifier;

abstract class SuperClass { //부모 클래스
	public void methodA() {
		System.out.println("methodA() 실행");
	}
	
	public abstract void methodB();
}

class SubClass extends SuperClass { //자식클래스
	/* 컴파일 에러
	 * 부모 클래스로부터 methodA(), methodB()상속
	 * 자식 클래스에는 구현되지 않은 methodB()가 추상 메서드로 있는 것과 동일
	 * 자식 클래스인 SubClass를 추상 클래스로 선언해야함
	 * but SubClass 객체를 생성할 수 없는 클래스가 됨
	 * SubClass 객체 생성할 수 있게 하려면 methodB()를 Overriding 해야함
	 */
}