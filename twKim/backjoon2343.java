import java.util.Scanner;

public class backjoon2343 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int [] array = new int [N];
		
		int start = 0;
		int end = 0;
		
		for(int i=0; i < N; i++) {
			array[i] = sc.nextInt();
			if(start < array[i]) {
				start = array[i];
			}
			end = end + array[i];
		}
		
		while(start <= end) {
			int middle = (start + end) / 2;
			int sum = 0;
			int count = 0;
			for(int i=0; i < N; i++) {
				if(sum + array[i] > middle) {
					count++;
					sum = 0;
				}
				sum = sum + array[i];
			}
			if(sum != 0) {
				count++;
			}
			if(count > M) {
				start = middle + 1;
			}
			else {
				end = middle - 1;
			}
		}
		
		//System.out.println(Arrays.toString(array));
		//System.out.println(min_n);
		System.out.println(start);
	}
}
