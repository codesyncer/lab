import java.util.Scanner;
class Product{
	static final int offset = 100;
	static float total = 0;
	static void printList(Product[] list){
		for(Product product : list){
			product.print();
		}
	}
	static void printListQ(Product[] list){
		for(Product product : list){
			product.printQ();
		}
	}
	static Product[] get(Scanner sc, int n){
		Product[] list = new Product[n];
		for(int i=0; i<n; ++i){
			System.out.printf("\nName of product : ");
			String name = sc.next();
			System.out.printf("Unit price : ");
			float uPrice = sc.nextFloat();
			list[i] = new Product(name, uPrice, i);
		}
		return list;
	}
	static void getQ(Scanner sc, Product[] list, int n, int nn){
		Product.total = 0;
		for(int i =0; i<n; ++i){
			System.out.printf("\nID : ");
			int id = sc.nextInt();
			System.out.printf("Quantity : ");
			int q = sc.nextInt();
			id -= Product.offset;
			if(id>=0 && id< nn){
				list[id].setQ(q);
				total += list[id].totalMe();
			}
			else{
				System.out.println("No such product");
			}
		}
	}
	String name;
	int id;
	float unitPrice;
	int quantity;
	Product(String name, float price, int id){
		this.name = name;
		unitPrice = price;
		this.id = Product.offset + id;
		quantity = 0;
	}
	void setQ(int q){
		quantity = q;
	}
	void print(){
		System.out.printf("%-5d\t%-10s\t%-7.2f\n", id, name, unitPrice);
	}
	void printQ(){
		if(quantity != 0)
			System.out.printf("%-5d\t%-10s\t%-7.2f\t%-5d\n", id, name, unitPrice, quantity);
	}
	float totalMe(){
		return quantity*unitPrice;
	}
	static void printHeader(){
		System.out.printf("\n%-5s\t%-10s\t%-7s\n", "ID", "NAME", "UPRICE");
	}
	static void printHeaderQ(){
		System.out.printf("\n%-5s\t%-10s\t%-7s\t%-5s\n", "ID", "NAME", "UPRICE","QNT");
	}
}
class p1{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int MAX = 10;
		System.out.print("Enter number of products : ");
		int n = Math.min(sc.nextInt(), MAX);
		Product[] list = Product.get(sc, n);
		Product.printHeader();
		Product.printList(list);
		System.out.print("\nEnter number of products : ");
		int sn = Math.min(sc.nextInt(), n);
		Product.getQ(sc, list, sn, n);
		Product.printHeaderQ();
		Product.printListQ(list);
		System.out.printf("\nTotal : Rs %.2f\n", Product.total);
	}
}