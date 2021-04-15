class Shape {
	int x=0, y=0;
	Shape() { // �⺻������
		this(0,0); // x=0, y=0
	}
	Shape(int x, int y) { // x,y�� �Ű������� ���� x,y������ �ʱ�ȭ
		this.x=x;
		this.y=y;
	}
}

class Circle extends Shape {
	int rad;
	Circle(int x, int y, int rad) {
		super(x,y); // �θ� Ŭ������ Shape(int x, int y) �����ڸ� ����� ȣ��
		// super(x,y) ������ �⺻������ ȣ��Ǿ� x=0, y=0��
		this.rad = rad;
	}
	public void draw() {
		System.out.println(x + ", " + y + " ��ǥ�� �������� " + rad + 
				"�� ���� �׸���.");
	}
}
public class SuperConstructorTest {

	public static void main(String[] args) {
		Circle c = new Circle(200,500,100);
		c.draw();

	}

}
