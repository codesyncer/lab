class Connector{
	int length;
	Connector(int length){
		this.length = length;
	}
	protected void finalize(){
		System.out.println("length = "+length);
		System.out.println("Object dying! Closing connection!");
		forceCloseAny();
	}
	void forceCloseAny(){

	}
}
class p4{
	public static void main(String args[]){
		new Connector(10);
		System.out.println("Calling GC");
		System.gc();
	}
}