package finalModifier;
class Car {
	String name;
	int speed;
	public final void printInfo() { // final 메서드 사용
		System.out.println(name + "의 현재 속도 : " + speed);
	}
}
class Taxi extends Car {
	int currentOil;
	public void printInfo() { // 메서드 overriding 불가
		System.out.println(name + "의 현재 속도 : " + speed);
		System.out.println(name + "의 현재 연료 : " + currentOil);

	}
}
