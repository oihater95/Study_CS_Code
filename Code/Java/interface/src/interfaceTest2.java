interface Paintable {
	public void paint();
}

interface Drawable2 { // Drawable �������̽� ����
	public int PLAIN_PEN = 1 ;// ��� ���� �������
	public int BOLD_PEN = 2;
	public int ITALIC_PEN = 3;
	public void draw(); // �߻�޼���
	public void move(int x, int y);
}

interface Printable extends Paintable, Drawable2 {
	public void print();
}


class Circle2 implements Printable {
	
	public void draw() {
		System.out.println("���� �׸��ϴ�.");
	}
	public void move(int x, int y) {
		System.out.println("���� �̵��մϴ� : (" + x + ", " + y + ")");
	}
	public void paint() {
		System.out.println("���� ��ĥ�մϴ�.");
	}
	public void print() {
		System.out.println("���� ����մϴ�.");
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
