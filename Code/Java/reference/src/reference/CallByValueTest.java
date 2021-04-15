package reference;

public class CallByValueTest {

	public static void main(String[] args) {
		int score = 10; // score 변수에 10 초기화
		System.out.println("변경 전 score : " + score);
		
		// change메서드 호출하면서 score변수 값을 change메서드 매개변수로 선언된 score 변수에 복사
		changeScore(score); 
		
		// change메서드의 매개변수 score가 아닌 원래 scroe 변수 값 출력
		System.out.println("변경 후 score : " + score);
	}
	
	private static int changeScore(int score) {
		score = 100; // 매개 변수로 넘어온 score 변수 값을 100으로 수정
		System.out.println("변경된 score : " + score);
		return score; // 변경된 매개변수 score 변수 값 리턴
	}
}
