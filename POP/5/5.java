class MutualFund{
	final class Customer{
		int aadhar;
	}
	Customer customer;
	class 
    final void printWarning(){
		System.out.println("Mutual funds are subject to market risks.\nRead all scheme related docs carefully.");
    }
}
class myMutualFund extends MutualFund{
	/*class Custom extends Customer{
		int email;	
	}
	final void printWarning(){
		System.out.println("Mutual funds are not subject to market risks.");
	}*/
}
class p5{
	public static void main(String args[]){
		myMutualFund fund = new myMutualFund();
		fund.printWarning();
	}
}