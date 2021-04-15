package car;

public class Car {
	//��ü�� �Ӽ��� ��Ÿ���� ���� ����
	String name;
	int currentSpeed;
	int currentGear;
	
	// �޼��� ����
	void startEngine() {
		System.out.println("-> " + name + "�� �õ��� �Ҵ�.");
		currentSpeed = 1;
	}
	
	void changeGear(int gear) {
		System.out.println("-> �� " + gear + "������ �����Ѵ�.");
		currentGear = gear;
	}
	
	int getCurrentSpeed() {
		currentSpeed = currentSpeed + (currentGear*10);
		return currentSpeed;
	}
	
	void stopEngine() {
		System.out.println("-> " + name + "�� �õ��� ����.");
		currentSpeed = 0;
		currentGear = 0;
	}
	
	String getCurrentState() {
		return name + "�� ���� �ӵ� : " + getCurrentSpeed();
	}

}
