class SuperClass {
	int num1;
	public SuperClass() { // �θ�Ŭ���� ������ ȣ��� num1=100�ʱ�ȭ, �Ű��������� �⺻������
		System.out.println("SuperClass ��ü ����");
		num1 = 100;
	}
}

class SubClass extends SuperClass {
	int num2;
	public SubClass() { // �ڽ�Ŭ���� ������ ȣ��� num2=10000�ʱ�ȭ
		System.out.println("SubClass ��ü ����");
		num2 = 10000;
	}
}
public class ConstructorTest {

	public static void main(String[] args) {
		SubClass sub = new SubClass(); // �ڽ�Ŭ���� ��ü �����Ͽ� ���� �� ���
		System.out.println(sub.num1);
		System.out.println(sub.num2); 
		/* �θ� Ŭ���� ��ü�� �����Ǳ� ���ؼ��� �θ� Ŭ���� �����ڰ� ȣ��Ǿ����
		 * �ڽ� Ŭ�������� ��𿡵� �θ� Ŭ���� �����ڴ� ����, �θ�Ŭ������ �⺻�����ڰ� �ڵ����� ȣ���
		 * �θ� Ŭ������ �⺻ ������ ���� ��� �����߻�*/
		 
	}

}
