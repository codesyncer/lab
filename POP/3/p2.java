import java.util.Scanner;
class p2{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter size : ");
		int n = scan.nextInt();
		System.out.print("Enter elements : ");
		int sum = 0;
		for(int i=0;i<n;++i){
			int num = scan.nextInt();
			if(num>=10 && num<=99){
				sum += num;
			}
		}
		System.out.println(sum==30?"True":"False");
	}
}