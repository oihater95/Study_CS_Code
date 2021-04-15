package abstractModifier;
abstract class TV {
	public abstract void powerOn();
	public abstract void powerOff();
	public abstract void volumeUp();
	public abstract void volumeDown();
}

class S_TV extends TV { // �߻�Ŭ���� TV�� �θ���ϴ� Ŭ����, 
	//TVŬ������ ���ǵ� �߻� �޼��带������ Overriding�Ͽ� ����
	public void powerOn() {
		System.out.println("S_TV ---- ������ �Ҵ�.");
	}
	public void powerOff() {
		System.out.println("S_TV ---- ������ ����.");
	}
	public void volumeUp() {
		System.out.println("S_TV ---- �Ҹ��� ���δ�.");
	}
	public void volumeDown() {
		System.out.println("S_TV ---- �Ҹ��� �����.");
	}
}

class L_TV extends TV {// �߻�Ŭ���� TV�� �θ���ϴ� Ŭ����, 
	//TVŬ������ ���ǵ� �߻� �޼��带������ Overriding�Ͽ� ����
	public void powerOn() {
		System.out.println("L_TV ---- ������ �Ҵ�.");
	}
	public void powerOff() {
		System.out.println("L_TV ---- ������ ����.");
	}
	public void volumeUp() {
		System.out.println("L_TV ---- �Ҹ��� ���δ�.");
	}
	public void volumeDown() {
		System.out.println("L_TV ---- �Ҹ��� �����.");
	}
}

public class AbstractTVUser {

	public static void main(String[] args) {
		S_TV tv = new S_TV();
		// L_TV tv = new L_TV();
		tv.powerOn();
		tv.volumeUp();
		tv.volumeDown();
		tv.powerOff();

	}

}
