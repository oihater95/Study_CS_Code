package reference;

public class CallByReferenceTest {

	public static void main(String[] args) {
		int[] scoreList = {40, 78, 98}; // change�޼����� scoreList�� ������ ��ü �ּ� �� ����
		// ������ �迭 scoreList�� ���� 3���� ����� ������ �迭 ��ü �����Ͽ� �Ҵ�
		System.out.println("reference address1 : " + scoreList);
		changeScore(scoreList);
		
		System.out.println("���� �� score : " + scoreList[0]);
		changeScore2(scoreList); // change2�޼��� ȣ���ϸ鼭 scoreList ������ ���ڷ� �ѱ�
		System.out.println("���� �� score : " + scoreList[0]); // change2�޼��� ȣ�� �Ŀ� 0�� �ε��� �� ���

		
	}
	
	private static void changeScore(int[] scoreList) {
		System.out.println("reference address2 : " + scoreList);
		// main�� scoreList�� ������ ��ü �ּ� �� ����
	}
	
	private static int[] changeScore2(int[] scoreList) {
		scoreList[0] = 100; // scoreList ������ �����ϴ� ��ü�� 0�� �ε��� �� ����
		System.out.println("����� score : " + scoreList[0]);
		/* scoreList ������ �����ϴ� ��ü�� 0�� �ε����� ����Ǿ� main() �޼����� scoreList ������ �����ϴ� �迭 ��ü�� 
		������ ��ü�̹Ƿ� main() �޼��忡�� �迭�� ���� ����ϸ� ����� ���� ��µ� */
		
		return scoreList; // �迭 ����� ��ü ����
	}
}