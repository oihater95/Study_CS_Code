package reference;

public class CallByReferenceTest {

	public static void main(String[] args) {
		int[] scoreList = {40, 78, 98}; // change메서드의 scoreList와 동일한 객체 주소 값 가짐
		// 정수형 배열 scoreList에 정수 3개가 저장된 일차원 배열 객체 생성하여 할당
		System.out.println("reference address1 : " + scoreList);
		changeScore(scoreList);
		
		System.out.println("변경 전 score : " + scoreList[0]);
		changeScore2(scoreList); // change2메서드 호출하면서 scoreList 변수를 인자로 넘김
		System.out.println("변경 후 score : " + scoreList[0]); // change2메서드 호출 후에 0번 인덱스 값 출력

		
	}
	
	private static void changeScore(int[] scoreList) {
		System.out.println("reference address2 : " + scoreList);
		// main의 scoreList와 동일한 객체 주소 값 가짐
	}
	
	private static int[] changeScore2(int[] scoreList) {
		scoreList[0] = 100; // scoreList 변수가 참조하는 객체의 0번 인덱스 값 수정
		System.out.println("변경된 score : " + scoreList[0]);
		/* scoreList 변수가 참조하는 객체의 0번 인덱스가 변경되어 main() 메서드의 scoreList 변수가 참조하는 배열 객체도 
		동일한 객체이므로 main() 메서드에서 배열의 값을 출력하면 변경된 값이 출력됨 */
		
		return scoreList; // 배열 변경된 객체 리턴
	}
}
