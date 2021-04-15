package finalModifier;

public class finalTest {
	double flexibleRate = 43.44; // 일반변수 -> changeRate() 메서드에서 값 변경 가능
	final double fixedRate = 45.56; // final로 선언된 상수
	
	public void changeRate() {
		flexibleRate = 45.78;
		fixedRate = 45.99; // final로 생성된 변수값은 변경 불가
	}
	

}
