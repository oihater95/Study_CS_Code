class Dice {
	public static int dotCount = 5; // Ŭ���� ����
	public int rollingCount = 0; // �ν��Ͻ� ����
	
	public static void playGame() { // Ŭ���� �޼���
		dotCount++;		// Ŭ���� ���� dotCount�� playGame() �޼��忡�� ���� ����
		rollingCount++; // �ν��Ͻ� ���� rollingCount�� playGame() �޼��忡�� ���� �Ұ�
		System.out.println("������ ���� : " + rollingDice());
		// �Ϲ� �޼���� ����� rollingDice()�� Ŭ���� �޼����� playGame()���� ȣ�� �Ұ�
	}
	
	public int rollingDice() {
		int generatedNum = (int)(Math.random()*6)+1;
		return generatedNum;
	}
}
public class StaticMethodTest {

	public static void main(String[] args) {
		Dice.playGame();

	}

}
