class Printer {
	String name;
	int sheets;
	public void ready() {
		System.out.println(name + "�����͸� �����մϴ�.");
	}
	public final void printLogic() { // overring ������Ŵ
		ready();
		for (int i=0; i<3; i++) {
			System.out.println(name + "�� " + sheets + "�� �� ����մϴ�.");
			
		}
		close();
	}
	public void close() {
		System.out.println(name + "�����͸� �����մϴ�.");
	}
}

class DotPrinter extends Printer {
	int batteryGage;
	
	/*public void printLogic() { // overriding
		for (int i=0; i<3; i++) {
			System.out.println(name + "�� " + sheets + "�� �� ����մϴ�.");
		} // ready(), close() ��� �����߻�
		System.out.println("���� ���͸� : " + batteryGage + "%");
	} �޼��� overriding���� �߻��� ���� final�� ����Ͽ� ������ ��ӹ޵�����*/
	
}

public class OverridingTest2 {

	public static void main(String[] args) {
		DotPrinter p = new DotPrinter();
		p.name = "P308";
		p.sheets = 2;
		p.batteryGage = 80;
		p.printLogic();

	}

}
