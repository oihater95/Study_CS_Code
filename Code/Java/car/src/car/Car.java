package car;

public class Car {
	//객체의 속성을 나타내는 변수 선언
	String name;
	int currentSpeed;
	int currentGear;
	
	// 메서드 선언
	void startEngine() {
		System.out.println("-> " + name + "의 시동을 켠다.");
		currentSpeed = 1;
	}
	
	void changeGear(int gear) {
		System.out.println("-> 기어를 " + gear + "단으로 변경한다.");
		currentGear = gear;
	}
	
	int getCurrentSpeed() {
		currentSpeed = currentSpeed + (currentGear*10);
		return currentSpeed;
	}
	
	void stopEngine() {
		System.out.println("-> " + name + "의 시동을 끈다.");
		currentSpeed = 0;
		currentGear = 0;
	}
	
	String getCurrentState() {
		return name + "의 현재 속도 : " + getCurrentSpeed();
	}

}
