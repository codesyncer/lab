import java.util.Scanner;
public class p1{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter in format A op B : ");
		float a = scan.nextFloat();
		char op = scan.next().charAt(0);
		float b = scan.nextFloat();
		float res = -1;
		switch(op){
			case '+':
				res = a+b;
				break;
			case '-':
				res = a-b;
				break;
			case 'x':
				res = a*b;
				break;
			case '/':
				if(b==0)
					break;
				res = a/b;
				break;
			case '%':
				if(b==0)
					break;
				res = a%b;
				break;
		}
		if(res==-1)
			System.out.println("Invalid input");
		else
			System.out.printf("%.3f %c %.3f = %.3f\n",a,op,b,res);
		scan.close();
	}
}