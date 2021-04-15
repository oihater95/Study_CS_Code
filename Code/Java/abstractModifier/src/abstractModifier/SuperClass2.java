package abstractModifier;

abstract class SuperClass2 { //부모 클래스
	public void methodA() {
		System.out.println("methodA() 실행");
	}
	
	public abstract void methodB();
}

class SubClass2 extends SuperClass2 { //자식클래스
	public void methodB() // 자식클래스에서 추상 메서드 재정의(Overriding)
	{
		System.out.println("methodB() 실행");
	}
}