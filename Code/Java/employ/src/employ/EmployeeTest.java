package employ;
// �ν��Ͻ� ������ ���� �޸� ���� ����

// Employee Ŭ���� ����
class Employee2 {
	String name;
	int employeeNo;
	int age;
	String companyName; // ������ �� ���� ���� 
	//-> �ν��Ͻ� ������ �ƴ� Ŭ���� ������ �����ϴ� ���� �޸𸮻� ����
}

// Employee Ŭ���� ��ü ���� �� �� �Ҵ�
public class EmployeeTest {
	public static void main(String[] args) {
		Employee2 kim = new Employee2();
		kim.name = "������";
		kim.employeeNo = 12345;
		kim.age = 45;
		kim.companyName = "S����";
		
		Employee2 lee = new Employee2();
		lee.name = "�̼���";
		lee.employeeNo = 12346;
		lee.age = 39;
		lee.companyName = "S����";
		
		Employee2 park = new Employee2();
		park.name = "���缺";
		park.employeeNo = 12347;
		park.age = 28;
		park.companyName = "S����";

	}

}
