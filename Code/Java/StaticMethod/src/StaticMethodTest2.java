class Dice2 {
	public static int dotCount = 5; // Ŭ���� ����
	public static int rollingCount = 0; // Ŭ���� ����
	
	public static void playGame() { // Ŭ���� �޼���
		dotCount++;		// Ŭ���� ���� dotCount�� playGame() �޼��忡�� ���� ����
		rollingCount++; // Ŭ���� ���� rollingCount�� playGame() �޼��忡�� ���� ����
		System.out.println("������ ���� : " + rollingDice());
		// Ŭ���� �޼���� ����� rollingDice()�� Ŭ���� �޼����� playGame()���� ȣ�� ����
	}
	
	public static int rollingDice() {
		int generatedNum = (int)(Math.random()*6)+1;
		return generatedNum;
	}
}
public class StaticMethodTest2 {

	public static void main(String[] args) {
		Dice2.playGame();

	}

}
