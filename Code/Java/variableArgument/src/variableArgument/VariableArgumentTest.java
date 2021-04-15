package variableArgument;

public class VariableArgumentTest {
	public static int intSum(int... num) {
		// 가변적 매개변수는 매개변수 리스트 마지막 위치에 딱 한번만 사용가능
		int sum = 0;
		for(int i = 0; i<num.length; i++) {
			sum = sum+num[i];
		}
		return sum;
	}
	public static void main(String[] args) {
		System.out.println(intSum(1));
		System.out.println(intSum(1,2));
		System.out.println(intSum(1,2,3));
	}

}
