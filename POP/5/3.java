class Pair{
	int a,b;
	static void swap(Pair x){
		int temp = x.a;
		x.a = x.b;
		x.b = temp;
	}
	Pair(int a, int b){
		this.a = a;
		this.b = b;
	}
	void swapNpush(int a, int b){
		this.a = a;
		this.b = b;	
		swap();
	}
	void swap(){
		int temp = a;
		a = b;
		b = temp;	
	}
	int getFirst(){
		return a;
	}
	int getSecond(){
		return b;
	}
}
class p3{
	public static void main(String args[]){
		int a = 10, b = 20;
		System.out.println("Before swapping");
		System.out.printf("a: %d\tb: %d\n", a, b);
		Pair pair = new Pair(a, b);
		Pair.swap(pair);
		a = pair.getFirst();
		b = pair.getSecond();
		System.out.println("After swapping");
		System.out.printf("a: %d\tb: %d\n", a, b);

		a = 10; b = 20;
		System.out.println("Before swapping");
		System.out.printf("a: %d\tb: %d\n", a, b);
		pair.swapNpush(a,b);
		a = pair.getFirst();
		b = pair.getSecond();
		System.out.println("After swapping");
		System.out.printf("a: %d\tb: %d\n", a, b);
	}
}