package finalModifier;
class Car {
	String name;
	int speed;
	public final void printInfo() { // final �޼��� ���
		System.out.println(name + "�� ���� �ӵ� : " + speed);
	}
}
class Taxi extends Car {
	int currentOil;
	public void printInfo() { // �޼��� overriding �Ұ�
		System.out.println(name + "�� ���� �ӵ� : " + speed);
		System.out.println(name + "�� ���� ���� : " + currentOil);

	}
}
