class Shape {
	int x=0, y=0;
	Shape() { // 기본생성자
		this(0,0); // x=0, y=0
	}
	Shape(int x, int y) { // x,y를 매개변수로 받은 x,y값으로 초기화
		this.x=x;
		this.y=y;
	}
}

class Circle extends Shape {
	int rad;
	Circle(int x, int y, int rad) {
		super(x,y); // 부모 클래스의 Shape(int x, int y) 생성자를 명시적 호출
		// super(x,y) 없으면 기본생성자 호출되어 x=0, y=0됨
		this.rad = rad;
	}
	public void draw() {
		System.out.println(x + ", " + y + " 좌표에 반지름이 " + rad + 
				"인 원을 그린다.");
	}
}
public class SuperConstructorTest {

	public static void main(String[] args) {
		Circle c = new Circle(200,500,100);
		c.draw();

	}

}
