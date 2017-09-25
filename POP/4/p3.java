class Number{
	public static String decToHex(int n){
		String str = "";
		int last;
		do{
			last = n%16;
			str = (char)(last + (last < 10 ? 48 : 65-10)) + str;
			n/=16;
		}while(n > 0);
		return "0x"+str;
	}
}
class p3{
	public static void main(String args[]){
		int num = 13303312;
		System.out.printf("%d in hex is %s\n", num, Number.decToHex(num));
	}
}