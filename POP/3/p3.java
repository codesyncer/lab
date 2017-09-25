import java.util.Scanner;
class p3{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter size : ");
		int n = scan.nextInt();
		System.out.print("Enter elements : ");
		int[] arr = new int[n];
		for(int i=0;i<n;++i)
			arr[i] = scan.nextInt();
		System.out.print("Enter element : ");
		int ele = scan.nextInt();
		boolean found = false;
		System.out.print("Found at :");		
		for(int i =0; i<n; ++i)
			if(arr[i]==ele){
				System.out.print(" " + i);
				found = true;
			}
		if(!found)
			System.out.print(" not found");
		System.out.println();		
	}
}