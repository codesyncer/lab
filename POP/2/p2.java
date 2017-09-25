import java.util.Scanner;
public class p2{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Input the investment amount: ");
		float p = scan.nextFloat();
		System.out.print("Input the rate of interest: ");
		float r = scan.nextFloat();
		System.out.print("Input number of years: ");
		int y = scan.nextInt();
		System.out.println("Years\tFuture Value");
		for(int i = 1; i <= y; ++i){
			System.out.printf("%-5d\t%.2f\n", i, p*Math.pow(1+r/1200f, i*12));
		}
		scan.close();
	}
}