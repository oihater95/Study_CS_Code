class Printer {
	String name;
	int sheets;
	public void ready() {
		System.out.println(name + "프린터를 예열합니다.");
	}
	public final void printLogic() { // overring 금지시킴
		ready();
		for (int i=0; i<3; i++) {
			System.out.println(name + "로 " + sheets + "장 씩 출력합니다.");
			
		}
		close();
	}
	public void close() {
		System.out.println(name + "프린터를 종료합니다.");
	}
}

class DotPrinter extends Printer {
	int batteryGage;
	
	/*public void printLogic() { // overriding
		for (int i=0; i<3; i++) {
			System.out.println(name + "로 " + sheets + "장 씩 출력합니다.");
		} // ready(), close() 없어서 문제발생
		System.out.println("현재 배터리 : " + batteryGage + "%");
	} 메서드 overriding으로 발생할 문제 final을 사용하여 무조건 상속받도록함*/
	
}

public class OverridingTest2 {

	public static void main(String[] args) {
		DotPrinter p = new DotPrinter();
		p.name = "P308";
		p.sheets = 2;
		p.batteryGage = 80;
		p.printLogic();

	}

}
