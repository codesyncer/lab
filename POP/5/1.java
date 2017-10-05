class Person{
	String name;
	int age;
	Person(String name, int age){
		this.name = name;
		this.age = age;
	}
	void printName(){
		System.out.print(name);
	}
}
class Employee extends Person{
	static int idGen = 1001;
	String post;
	int id;
	float pay;
	int service;
	Employee(String name, int age, String post){
		super(name, age);
		id = idGen++;
		this.post = post;
		service = (int)Math.random()*30; 
		calcPay();
	}
	void calcPay(){
		pay = post.length()*1000;
		pay += service*100;

	}
	void print(){
		System.out.println();
		printName();
		System.out.printf("(%d)\n", id);
		System.out.println("Pay : Rs "+pay);
	}
}
class p1{
	public static void main(String args[]){
		new Employee("Srinag", 20, "Gaurd").print();
		new Employee("Skitty", 29, "Manager").print();
		new Employee("Mon", 50, "Big post this is").print();
	}	
}