package car;
class Car2 {
	String name;
	int speed;
	public void printInfo() {
		System.out.println(name + "�� ���� �ӵ� : " + speed);
	}
}
public class Taxi extends Car2 {

	// ���
	int fare;
	// �°� ����
	boolean passengerYn;
	int currentOil;
	public void printInfo() { // �޼��� overriding
		System.out.println(name + "�� ���� �ӵ� : " + speed);
		System.out.println(name + "�� ���� ���� : " + currentOil);
	}
}
