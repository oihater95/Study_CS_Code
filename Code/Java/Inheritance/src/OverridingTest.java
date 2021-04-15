class Camera {
	String name;
	int sheets;
	public void takePicture() {
		System.out.println(name + "로 " + sheets + "번 사진을 찍는다.");
	}
}
 
class PolaroidCamera extends Camera {
	int batteryGage;
	public void takePicture() { // 메서드 overriding, 부모 클래스의 takePicture메서드는 상속되지않음
		// System.out.println(name + "로 " + sheets + "번 사진을 찍는다."); -> 부모 클래스의 메서드와 중복
		super.takePicture(); // 중복되는 부분은 부모클래스의 메서드 명시적으로 호출 -> 메서드 overriding 하면서 부모클래스 메서드사용
		System.out.println(sheets + "장의 사진을 프린트한다.");
		System.out.println("현재 배터리 : " + batteryGage + "%");
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
