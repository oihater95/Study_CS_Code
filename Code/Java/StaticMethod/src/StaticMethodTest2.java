class Dice2 {
	public static int dotCount = 5; // 클래스 변수
	public static int rollingCount = 0; // 클래스 변수
	
	public static void playGame() { // 클래스 메서드
		dotCount++;		// 클래스 변수 dotCount는 playGame() 메서드에서 접근 가능
		rollingCount++; // 클래스 변수 rollingCount는 playGame() 메서드에서 접근 가능
		System.out.println("생성된 숫자 : " + rollingDice());
		// 클래스 메서드로 선언된 rollingDice()는 클래스 메서드인 playGame()에서 호출 가능
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
