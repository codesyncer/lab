import java.util.Scanner;
public class p6{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Size of array: ");
		int n = scan.nextInt();
		if(n < 1){
			return;
		}
		System.out.print("Enter elements: ");
		int[] arr = new int[n];
		for(int i = 0; i < n; ++i)
			arr[i] = scan.nextInt();
		int tmp;
		for(int i = 0; i < n-1; ++i){
			for(int j = 0; j < n-i-1; ++j){
				if(arr[j]>arr[j+1]){
					tmp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = tmp;
				}
			}
		}
		int max = 0, min = Integer.MAX_VALUE, cLen = 0;
		for(int i = 1; i < n; ++i){
			if(arr[i] == arr[i-1] + 1)
				cLen++;
			else{
				min = cLen!=0 && min > cLen ? cLen : min; 
				max = max < cLen ? cLen : max;
				cLen = 0;
			}
		}
		max = max < cLen ? cLen : max;
		min = cLen!=0 && min > cLen ? cLen : min; 
		System.out.printf("Max length: %d\n", max==0 ? 0 : max+1);
		System.out.printf("Min length: %d\n", max==0 ? 0 : min+1);
		scan.close();
	}
}