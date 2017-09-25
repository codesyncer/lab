import java.util.Scanner;
class p1{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter a number : ");
		int num = scan.nextInt();
		String[] days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
		System.out.println(days[num>0 ? (num-1)%7 : 7 - (1-num)%7]);
	}
}