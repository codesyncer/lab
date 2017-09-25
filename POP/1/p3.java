import java.util.Scanner;
public class p3{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter A B C from equations in form Ax + By = C");
		float a1 = scan.nextFloat();
		float b1 = scan.nextFloat();
		float c1 = scan.nextFloat();
		float a2 = scan.nextFloat();
		float b2 = scan.nextFloat();
		float c2 = scan.nextFloat();
		if(a1/a2 == b1/b2 && c1/c2 == b1/b2){
			System.out.println("Infinite solutions");
		}
		else if(a1/b1 == a2/b2){
			System.out.println("No solution");
		}
		else{
			System.out.printf("x = %f and y = %f\n",(c1*b2-c2*b1)/(a1*b2-a2*b1),(c1*a2-c2*a1)/(b1*a2-b2*a1));
		}
		scan.close();
	}
}