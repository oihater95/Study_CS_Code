class Outside { // �ܺ� Ŭ���� , top level Ŭ����
	public class Inside { // ���� �Ѥ������� �Ϲ� ��� ������ ������ ��ġ�� ����
		
	}
	
	public static class StaticInner {
		
	}
}

class Animal {
	void performBehavior() { 
		//�̸��� �ִ� ���� ���� Ŭ����, ������ �� Animal$1$Brain.class����
		class Brain {
			
		}
	}
}
public class InnerClassTest {

	public static void main(String[] args) {
		Outside.StaticInner sinner = new Outside.StaticInner(); // static ���� Ŭ������ �ܺ� Ŭ���� ��ü �������� ��ü�������� 
		Outside outer = new Outside();
		Outside.Inside inner = outer.new Inside();
	}

}
// ������ ��
// �ܺ� Ŭ���� Outside.class / ���� Ŭ���� Outside$Inside.class ����
