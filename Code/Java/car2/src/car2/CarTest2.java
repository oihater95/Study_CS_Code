package car2;
//클래스 선언
class Car{
	private int serialNumber; // 중요한 데이터 접근 제한
	protected String name;
	int speed;
	
	// public 이지만 인증된 managerId에 대해서만 값 리턴
	public int getSerialNumber(int managerId) {
		if(managerId == 12345) {
			return serialNumber;
		}
		return 0;
	}
	// 어디에서든 호출하여 사용가능
	public void setserialNumber(int serialNumber) {
		this.serialNumber = serialNumber;
	}
	
}

public class CarTest2 {
	
	public static void main(String[] args) {
		Car Yellow = new Car();
		Yellow.name = "Lightning Yellow";
		Yellow.speed = 300;
		Yellow.setserialNumber(4929); // serialNumber 변수는 private이기 때문에 setSerial 사용
		System.out.println(Yellow.name + " : " + Yellow.speed);
		System.out.println("Car No : " + Yellow.getSerialNumber(12345));
	}

}
