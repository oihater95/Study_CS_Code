package abstractModifier;

abstract class SuperClass { //�θ� Ŭ����
	public void methodA() {
		System.out.println("methodA() ����");
	}
	
	public abstract void methodB();
}

class SubClass extends SuperClass { //�ڽ�Ŭ����
	/* ������ ����
	 * �θ� Ŭ�����κ��� methodA(), methodB()���
	 * �ڽ� Ŭ�������� �������� ���� methodB()�� �߻� �޼���� �ִ� �Ͱ� ����
	 * �ڽ� Ŭ������ SubClass�� �߻� Ŭ������ �����ؾ���
	 * but SubClass ��ü�� ������ �� ���� Ŭ������ ��
	 * SubClass ��ü ������ �� �ְ� �Ϸ��� methodB()�� Overriding �ؾ���
	 */
}