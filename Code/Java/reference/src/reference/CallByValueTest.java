package reference;

public class CallByValueTest {

	public static void main(String[] args) {
		int score = 10; // score ������ 10 �ʱ�ȭ
		System.out.println("���� �� score : " + score);
		
		// change�޼��� ȣ���ϸ鼭 score���� ���� change�޼��� �Ű������� ����� score ������ ����
		changeScore(score); 
		
		// change�޼����� �Ű����� score�� �ƴ� ���� scroe ���� �� ���
		System.out.println("���� �� score : " + score);
	}
	
	private static int changeScore(int score) {
		score = 100; // �Ű� ������ �Ѿ�� score ���� ���� 100���� ����
		System.out.println("����� score : " + score);
		return score; // ����� �Ű����� score ���� �� ����
	}
}
