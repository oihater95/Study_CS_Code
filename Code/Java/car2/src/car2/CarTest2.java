package car2;
//Ŭ���� ����
class Car{
	private int serialNumber; // �߿��� ������ ���� ����
	protected String name;
	int speed;
	
	// public ������ ������ managerId�� ���ؼ��� �� ����
	public int getSerialNumber(int managerId) {
		if(managerId == 12345) {
			return serialNumber;
		}
		return 0;
	}
	// ��𿡼��� ȣ���Ͽ� ��밡��
	public void setserialNumber(int serialNumber) {
		this.serialNumber = serialNumber;
	}
	
}

public class CarTest2 {
	
	public static void main(String[] args) {
		Car Yellow = new Car();
		Yellow.name = "Lightning Yellow";
		Yellow.speed = 300;
		Yellow.setserialNumber(4929); // serialNumber ������ private�̱� ������ setSerial ���
		System.out.println(Yellow.name + " : " + Yellow.speed);
		System.out.println("Car No : " + Yellow.getSerialNumber(12345));
	}

}
