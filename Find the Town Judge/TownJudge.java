
import java.io.IOException;

public class TownJudge {
	
	public static int isJudge(int [][] A,int N) {
		if (A.length==0) return 1;
		int map[][] = new int[N][2];
		for(int i =0;i<A.length;i++) {
			map[A[i][0]-1][0]+=1;
			map[A[i][1]-1][1]+=1;
		}
		
		for(int i =0;i<N;i++) {
			if(map[i][0]==0 && map[i][1]==N-1) return i+1;
		}
		return -1;
		
	}
	
	public static void main(String[] args) throws IOException {
		int A[][] = {{1,3},{1,4},{2,3},{2,4},{4,3}};
		int N = 4;
		System.out.println(isJudge(A,N));
	}
}
