interface Paintable {
	public void paint();
}

interface Drawable2 { // Drawable 인터페이스 정의
	public int PLAIN_PEN = 1 ;// 멤버 변수 상수선언
	public int BOLD_PEN = 2;
	public int ITALIC_PEN = 3;
	public void draw(); // 추상메서드
	public void move(int x, int y);
}

interface Printable extends Paintable, Drawable2 {
	public void print();
}


class Circle2 implements Printable {
	
	public void draw() {
		System.out.println("원을 그립니다.");
	}
	public void move(int x, int y) {
		System.out.println("원을 이동합니다 : (" + x + ", " + y + ")");
	}
	public void paint() {
		System.out.println("원을 색칠합니다.");
	}
	public void print() {
		System.out.println("원을 출력합니다.");
	}
}


public class interfaceTest2 {

	public static void main(String[] args) {
		Circle2 c = new Circle2();
		c.draw();
		c.move(5, 5);
		c.paint();
		c.print();

	}

}
