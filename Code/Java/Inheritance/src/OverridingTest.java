class Camera {
	String name;
	int sheets;
	public void takePicture() {
		System.out.println(name + "�� " + sheets + "�� ������ ��´�.");
	}
}
 
class PolaroidCamera extends Camera {
	int batteryGage;
	public void takePicture() { // �޼��� overriding, �θ� Ŭ������ takePicture�޼���� ��ӵ�������
		// System.out.println(name + "�� " + sheets + "�� ������ ��´�."); -> �θ� Ŭ������ �޼���� �ߺ�
		super.takePicture(); // �ߺ��Ǵ� �κ��� �θ�Ŭ������ �޼��� ���������� ȣ�� -> �޼��� overriding �ϸ鼭 �θ�Ŭ���� �޼�����
		System.out.println(sheets + "���� ������ ����Ʈ�Ѵ�.");
		System.out.println("���� ���͸� : " + batteryGage + "%");
	}
}
public class OverridingTest {
	public static void main(String[] args) {
		PolaroidCamera cam = new PolaroidCamera();
		cam.name = "X-508";
		cam.sheets = 3;
		cam.batteryGage = 57;
		cam.takePicture();
	}

}