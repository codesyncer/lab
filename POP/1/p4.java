import java.util.Scanner;
public class p4{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter A and B : ");
		int a = scan.nextInt();
		int b = scan.nextInt();
		System.out.printf("Rightshift Unsigned %d>>>%d = %d\n",a,b,a>>>b);
		System.out.printf("Rightshift %d>>%d = %d\n",a,b,a>>b);
		System.out.printf("Leftshift %d<<%d = %d\n",a,b,a<<b);
		scan.close();
	}
}