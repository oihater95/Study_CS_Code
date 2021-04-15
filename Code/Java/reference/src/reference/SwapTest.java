package reference;
class Pair{
	int x;
	int y;
	Pair(int x, int y) {
		this.x = x;
		this.y = y;
	}
}


public class SwapTest {
	public static void swap(int x, int y) {
		int tmp;
		tmp = x;
		x = y;
		y = tmp;
		// int 유형의 매개변수를 입력받아 그 값을 바꾸는 swap메서드
	}
	
	public static void swap(Pair p) {
		int tmp;
		tmp = p.x;
		p.x = p.y;
		p.y = tmp;
		// Pair 객체를 매개변수로 입력 받아 객체 변수 값을 서로 바꾸는 swap 메서드 overloading
	}

	public static void main(String[] args) {
		// x, y 값과 pair객체 초기화
		int x = 10, y=20;
		Pair p = new Pair(10, 20);
		
		System.out.println("before : x, y (" +x+", "+y+")");
		System.out.println("before : x, y (" +p.x+", "+p.y+")");
		
		//swap 메서드 호출
		swap(x,y);
		swap(p);
		
		System.out.println("before : x, y (" +x+", "+y+")");
		System.out.println("before : x, y (" +p.x+", "+p.y+")");
		/*x,y swap은 바뀌지 않았는데 이유는 메서드 안에서는 바뀌었지만 메서드에서의 x,y는 
		 * main의 x,y 값만 복사해온 것이라 main의 x,y는 바뀌지 않음
		 * 객체 p의 xy는 바뀌었는데 이유는 p의 xy와 메서드의 xy가 동일한 객체를 참조하고 있기 때문에
		 * 객체의 값을 바꾸면 둘다 바뀐 객체를 참조하여 바뀐 값이 출력됨*/
	}

}
