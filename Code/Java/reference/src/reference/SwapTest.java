package reference;
class Pair{
	int x;
	int y;
	Pair(int x, int y) {
		this.x = x;
		this.y = y;
	}
}


public class SwapTest {
	public static void swap(int x, int y) {
		int tmp;
		tmp = x;
		x = y;
		y = tmp;
		// int ������ �Ű������� �Է¹޾� �� ���� �ٲٴ� swap�޼���
	}
	
	public static void swap(Pair p) {
		int tmp;
		tmp = p.x;
		p.x = p.y;
		p.y = tmp;
		// Pair ��ü�� �Ű������� �Է� �޾� ��ü ���� ���� ���� �ٲٴ� swap �޼��� overloading
	}

	public static void main(String[] args) {
		// x, y ���� pair��ü �ʱ�ȭ
		int x = 10, y=20;
		Pair p = new Pair(10, 20);
		
		System.out.println("before : x, y (" +x+", "+y+")");
		System.out.println("before : x, y (" +p.x+", "+p.y+")");
		
		//swap �޼��� ȣ��
		swap(x,y);
		swap(p);
		
		System.out.println("before : x, y (" +x+", "+y+")");
		System.out.println("before : x, y (" +p.x+", "+p.y+")");
		/*x,y swap�� �ٲ��� �ʾҴµ� ������ �޼��� �ȿ����� �ٲ������ �޼��忡���� x,y�� 
		 * main�� x,y ���� �����ؿ� ���̶� main�� x,y�� �ٲ��� ����
		 * ��ü p�� xy�� �ٲ���µ� ������ p�� xy�� �޼����� xy�� ������ ��ü�� �����ϰ� �ֱ� ������
		 * ��ü�� ���� �ٲٸ� �Ѵ� �ٲ� ��ü�� �����Ͽ� �ٲ� ���� ��µ�*/
	}

}
