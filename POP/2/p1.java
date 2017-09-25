import java.util.Scanner;
public class p1{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Input first number: ");
		int a = scan.nextInt();
		System.out.print("Input second number: ");
		int b = scan.nextInt();
		System.out.print("Input third number: ");
		int c = scan.nextInt();
		if(a > b && b>c)
			System.out.println("Decreasing order");
		else if(a < b && b < c)
			System.out.println("Increasing order");
		else
			System.out.println("Neither increasing or decreasing order");
		scan.close();
	}
}