class Dice {
	public static int dotCount = 5; // 클래스 변수
	public int rollingCount = 0; // 인스턴스 변수
	
	public static void playGame() { // 클래스 메서드
		dotCount++;		// 클래스 변수 dotCount는 playGame() 메서드에서 접근 가능
		rollingCount++; // 인스턴스 변수 rollingCount는 playGame() 메서드에서 접근 불가
		System.out.println("생성된 숫자 : " + rollingDice());
		// 일반 메서드로 선언된 rollingDice()는 클래스 메서드인 playGame()에서 호출 불가
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
