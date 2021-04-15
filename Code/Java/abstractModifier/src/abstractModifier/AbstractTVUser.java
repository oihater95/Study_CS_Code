package abstractModifier;
abstract class TV {
	public abstract void powerOn();
	public abstract void powerOff();
	public abstract void volumeUp();
	public abstract void volumeDown();
}

class S_TV extends TV { // 추상클래스 TV를 부모로하는 클래스, 
	//TV클래스에 정의된 추상 메서드를적절히 Overriding하여 구현
	public void powerOn() {
		System.out.println("S_TV ---- 전원을 켠다.");
	}
	public void powerOff() {
		System.out.println("S_TV ---- 전원을 끈다.");
	}
	public void volumeUp() {
		System.out.println("S_TV ---- 소리를 높인다.");
	}
	public void volumeDown() {
		System.out.println("S_TV ---- 소리를 낮춘다.");
	}
}

class L_TV extends TV {// 추상클래스 TV를 부모로하는 클래스, 
	//TV클래스에 정의된 추상 메서드를적절히 Overriding하여 구현
	public void powerOn() {
		System.out.println("L_TV ---- 전원을 켠다.");
	}
	public void powerOff() {
		System.out.println("L_TV ---- 전원을 끈다.");
	}
	public void volumeUp() {
		System.out.println("L_TV ---- 소리를 높인다.");
	}
	public void volumeDown() {
		System.out.println("L_TV ---- 소리를 낮춘다.");
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
