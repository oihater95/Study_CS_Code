package finalModifier;

//static�� ���(Ŭ��������)�� �޸� ���� ���ϱ�
//Employee Ŭ���� ����
class Employee4 {
	String name;
	int employeeNo;
	int age;
	final static String COMPANY_NAME = "S����"; // ������ �� ���� ���� (Ŭ���� ����)
	//-> �ν��Ͻ� ������ �ƴ� Ŭ���� ������ �����ϴ� ���� �޸𸮻� ����
	// final ������ �����Ͽ� ��� ���(���� �Ұ�)
}

//Employee Ŭ���� ��ü ���� �� �� �Ҵ�
public class EmployeeTest_final_static  {
	public static void main(String[] args) {
		System.out.println("�������� ȸ��� : " + Employee4.COMPANY_NAME);
		Employee4.COMPANY_NAME = "A����" // final ���� ���� �� ����
	}

}