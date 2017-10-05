interface SeriesHolder{
	public void print();
	public void sum();
	public void gen();
}
class FibHolder implements SeriesHolder{
	int[] arr;
	int n;
	FibHolder(int n){
		arr = new int[n];
		this.n = n;
		gen();
	}
	public void print(){
		for(int i : arr)
			System.out.print(i+" ");
		System.out.println();
	}
	public void sum(){
		int sum=0;
		for(int i : arr)
			sum+=i;
		System.out.println(sum);	
	}
	public void gen(){
		arr[0] = 1;
		int prev = 0;
		for(int i=1; i<n; ++i){
			arr[i] = arr[i-1]+prev;
			prev = arr[i-1];
		}
	}
}
class APHolder implements SeriesHolder{
	int[] ap;
	int a, d, n;
	APHolder(int n, int a, int d){
		ap = new int[n];
		this.a = a;
		this.d = d;
		this.n=n;
		gen();
	}
	public void print(){
		System.out.print("AP: ");
		for(int i : ap)
			System.out.print(i+" ");
		System.out.println();
	}
	public void sum(){
		int sum=0;
		for(int i : ap)
			sum+=i;
		System.out.println("Sum is :"+sum);	
	}	
	public void gen(){
		ap[0] = a;
		for(int i=1; i<n; ++i)
			ap[i] = ap[i-1]+d;
	}
}

class p2{
	public static void main(String args[]){
		SeriesHolder fibo = new FibHolder(10);
		fibo.print();
		SeriesHolder ap = new APHolder(10, 1, 5);
		ap.print();
	}
}