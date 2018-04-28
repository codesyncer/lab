import java.util.Scanner;
public class p2{
	public static String toBinary(int n){
		String bin="";
		do{
			bin = (char)(48+n%2)+bin;
			n /= 2;
		}while(n!=0);
		return bin;
	}
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Decimal : ");
		int n = scan.nextInt();
		if(n < 0)
			System.out.println("Got -ve number");
		else
			System.out.println("Binary "+toBinary(n));
		scan.close();
	}
}