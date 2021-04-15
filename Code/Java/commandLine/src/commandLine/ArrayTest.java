package commandLine;

public class ArrayTest {

	public static void main(String[] args) {
		int[] javaScore = new int[5];
		
		javaScore[0] = Integer.parseInt(args[0]);
		javaScore[1] = Integer.parseInt(args[1]);
		javaScore[2] = Integer.parseInt(args[2]);
		javaScore[3] = Integer.parseInt(args[3]);
		javaScore[4] = Integer.parseInt(args[4]);
		
		int sumScore = 0;
		sumScore = javaScore[0] + javaScore[1] + javaScore[2] + javaScore[3] + javaScore[4];
		
		double avgScore = 0.0;
		avgScore = (double)sumScore/javaScore.length;
		
		System.out.println("자바 점수의 총합 : " + sumScore);
		System.out.println("자바 점수의 평균 : " + avgScore);;
	}

}
