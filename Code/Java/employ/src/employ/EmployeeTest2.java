package employ;
// static�� ���(Ŭ��������)�� �޸� ���� ���ϱ�

// Employee Ŭ���� ����
class Employee3 {
	String name;
	int employeeNo;
	int age;
	static String companyName = "S����"; // ������ �� ���� ���� (Ŭ���� ����)
	//-> �ν��Ͻ� ������ �ƴ� Ŭ���� ������ �����ϴ� ���� �޸𸮻� ����
}

// Employee Ŭ���� ��ü ���� �� �� �Ҵ�
public class EmployeeTest2  {
	public static void main(String[] args) {
		Employee3 kim = new Employee3();
		kim.name = "������";
		kim.employeeNo = 12345;
		kim.age = 45;
		
		Employee3 lee = new Employee3();
		lee.name = "�̼���";
		lee.employeeNo = 12346;
		lee.age = 39;
		
		Employee3 park = new Employee3();
		park.name = "���缺";
		park.employeeNo = 12347;
		park.age = 28;
		
		// Ŭ���� ���� �� ����
		// companyName = s����, ��� : s����
		System.out.println("kim�� ȸ��� : " + kim.companyName);
		
		// companyName = a���� �� ����, ��� : a����
		lee.companyName = "A����";
		System.out.println("lee�� ȸ��� : " + kim.companyName);
		
		// lee ���� ������ ���� a���ڷ� �����, ��� : a����
		System.out.println("park�� ȸ��� : " + kim.companyName);
	}

}
