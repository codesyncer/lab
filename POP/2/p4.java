import java.util.Scanner;
public class p4{
	static void sort(int[] arr, int n){
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
	}
	static boolean present(int x, int[] arr, int n){
		int l=0, r=n-1, mid;
		while(l <= r){
			mid = (l+r)/2;
			if(arr[mid] == x)
				return true;
			else if(x < arr[mid])
				r = mid - 1;
			else
				l = mid + 1;
		}
		return false;
	} 
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Size of array A: ");
		int na = scan.nextInt();
		if(na < 1)
			return;
		System.out.print("Enter elements: ");
		int[] a = new int[na];
		for(int i = 0; i < na; ++i)
			a[i] = scan.nextInt();
		System.out.print("Size of array B: ");
		int nb = scan.nextInt();
		if(nb < 1)
			return;
		System.out.print("Enter elements: ");
		int[] b = new int[nb];
		for(int i = 0; i < nb; ++i)
			b[i] = scan.nextInt();
		sort(b, nb);
		System.out.print("Common : ");
		for(int i = 0; i < na; ++i){
			if(present(a[i], b, nb)){
				System.out.printf("%d ", a[i]);
			}
		}
		System.out.print("\n");
		scan.close();
	}
}