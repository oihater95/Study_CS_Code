package abstractModifier;

abstract class SuperClass2 { //�θ� Ŭ����
	public void methodA() {
		System.out.println("methodA() ����");
	}
	
	public abstract void methodB();
}

class SubClass2 extends SuperClass2 { //�ڽ�Ŭ����
	public void methodB() // �ڽ�Ŭ�������� �߻� �޼��� ������(Overriding)
	{
		System.out.println("methodB() ����");
	}
}