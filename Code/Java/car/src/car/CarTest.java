package car;

public class CarTest {

	public static void main(String[] args) {
		// Car Instance ����(��ü ����)
		Car myCar = new Car();
		
		// �ʱ� �� ����
		myCar.name = "Red";
		myCar.currentGear = 0;
		myCar.currentSpeed = 0;
		
		// �޼��� ȣ��
		myCar.startEngine();
		System.out.println(myCar.getCurrentState());
		myCar.changeGear(2);
		System.out.println(myCar.getCurrentState());
		myCar.changeGear(3);
		System.out.println(myCar.getCurrentState());
		myCar.stopEngine();
		System.out.println(myCar.getCurrentState());
		
		System.out.println(""); 
		// Car instance ����(�ϳ��� Ŭ�����κ��� ���� ���� ��ü ����)
		Taxi myTaxi = new Taxi();
		// �ʱ� �� ����
		myTaxi.name = "���� ��� 308";
		myTaxi.currentGear = 2;
		myTaxi.fare = 3400;
		myTaxi.passengerYn = true;
		System.out.println(myTaxi.getCurrentState());
	}

}
