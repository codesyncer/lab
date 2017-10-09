class MutualFund{
	final class Customer{
		int aadhar;
	}
	Customer customer;
	String name;
	final void printWarning(){
    final void printWarning(){
		System.out.println("Mutual funds are subject to market risks.\nRead all scheme related docs carefully.");
    }
    MutualFund(String name){
		this.name = name;    	
    }
    void printName(){
    	System.out.println(name);
    }
}
class myMutualFund extends MutualFund{
	// class Custom extends Customer{
	// 	int email;	
	// }
	// final void printWarning(){
	// 	System.out.println("Mutual funds are not subject to market risks.");
	// }
	myMutualFund(String name){
		super(name);    	
    }
	void printName(){
		System.out.println("NITK/"+name);
	}
}
class p5{
	public static void main(String args[]){
		myMutualFund fund = new myMutualFund("NorthernTrust");
		fund.printWarning();
		fund.printName();
	}
}
