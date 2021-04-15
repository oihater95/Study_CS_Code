package car;
class Car2 {
	String name;
	int speed;
	public void printInfo() {
		System.out.println(name + "의 현재 속도 : " + speed);
	}
}
public class Taxi extends Car2 {

	// 요금
	int fare;
	// 승객 유무
	boolean passengerYn;
	int currentOil;
	public void printInfo() { // 메서드 overriding
		System.out.println(name + "의 현재 속도 : " + speed);
		System.out.println(name + "의 현재 연료 : " + currentOil);
	}
}
