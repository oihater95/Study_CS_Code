package car;

public class CarTest {

	public static void main(String[] args) {
		// Car Instance 생성(객체 생성)
		Car myCar = new Car();
		
		// 초기 값 설정
		myCar.name = "Red";
		myCar.currentGear = 0;
		myCar.currentSpeed = 0;
		
		// 메서드 호출
		myCar.startEngine();
		System.out.println(myCar.getCurrentState());
		myCar.changeGear(2);
		System.out.println(myCar.getCurrentState());
		myCar.changeGear(3);
		System.out.println(myCar.getCurrentState());
		myCar.stopEngine();
		System.out.println(myCar.getCurrentState());
		
		System.out.println(""); 
		// Car instance 생성(하나의 클래스로부터 여러 개의 객체 생성)
		Taxi myTaxi = new Taxi();
		// 초기 값 설정
		myTaxi.name = "대현 운수 308";
		myTaxi.currentGear = 2;
		myTaxi.fare = 3400;
		myTaxi.passengerYn = true;
		System.out.println(myTaxi.getCurrentState());
	}

}
