package variableArgument;

public class VariableArgumentTest {
	public static int intSum(int... num) {
		// ������ �Ű������� �Ű����� ����Ʈ ������ ��ġ�� �� �ѹ��� ��밡��
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
