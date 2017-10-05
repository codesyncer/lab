abstract class BankAc{
	float amount;
	BankAc(){
		amount = minimumBalance();
	}
	void deposit(float amount){
		this.amount += amount;
	}
	boolean withdraw(float amount){
		if(this.amount - amount >= minimumBalance()){
			this.amount -= amount;
			return true;
		}
		return false;
	}
	abstract float minimumBalance();
	abstract float intrestRate();
}
class SbiAc extends BankAc{
	float minimumBalance(){
		return 3000;
	}
	float intrestRate(){
		return 3;
	}
}
class CanaraAc extends BankAc{
	float minimumBalance(){
		return 1000;
	}
	float intrestRate(){
		return 5;
	}	
}
class p2{
	public static void main(String args[]){
		BankAc one = new SbiAc();
		one.deposit(5000);
		one.withdraw(3000);
		System.out.println("intrestRate at SBI : " + one.intrestRate());
		System.out.println("minimumBalance at SBI : " + one.minimumBalance());
		BankAc two = new CanaraAc();
		two.deposit(5000);
		two.withdraw(3000);
		System.out.println("intrestRate at Canara : " + two.intrestRate());
		System.out.println("minimumBalance at Canara : " + two.minimumBalance());
	}
}
