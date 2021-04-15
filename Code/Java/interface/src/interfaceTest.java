interface Drawable { // Drawable 인터페이스 정의
	public int PLAIN_PEN = 1; // 멤버 변수 상수선언
	public int BOLD_PEN = 2;
	public int ITALIC_PEN = 3;
	public void draw(); // 추상메서드
	public void move(int x, int y);
}

class Shape {
	int x = 0;
	int y = 0;
	
	Shape(int x, int y) {
		this.x = x;
		this.y =y ;
	}
}

class Circle extends Shape implements Drawable {
	int rad;
	Circle(int x, int y, int rad) {
		super(x,y);
		this.rad = rad;
	}
	
	public void draw() {
		System.out.println("(" + x +", " + y + ") rad = " + rad);
	}
	public void move(int x, int y) {
		System.out.println("(" + (this.x + x) + ", " + (this.y + y) + ") rad = " + rad);
	}
}

public class interfaceTest {

	public static void main(String[] args) {
		Circle c = new Circle(10, 10, 100);
		c.draw();
		c.move(5, 5);
		

	}

}
