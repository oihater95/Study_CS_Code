package finalModifier;

public class finalTest {
	double flexibleRate = 43.44; // �Ϲݺ��� -> changeRate() �޼��忡�� �� ���� ����
	final double fixedRate = 45.56; // final�� ����� ���
	
	public void changeRate() {
		flexibleRate = 45.78;
		fixedRate = 45.99; // final�� ������ �������� ���� �Ұ�
	}
	

}
