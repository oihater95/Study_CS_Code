
abstract class TV {
	public abstract void powerOn();
	public abstract void powerOff();
	public abstract void volumeUp();
	public abstract void volumeDown();
}


public class AnonymousTest {
public static void watchTV(Tv tv) {
		tv.powerOn();
		tv.volumeUp();
		tv.volumeDown();
		tv.powerOff();
	}
	public static void main(String[] args) {
		watchTV(new TV) {
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
		});
		
	}

}
