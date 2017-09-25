class Dept{
	public static final byte IT = 0, CSE = 1, ECE = 2, EEE = 3;
	public static final float[] bs = {10000f, 12000f, 9000f, 8500f};
	public static final String[] name = {"IT","CSE","ECE","EEE"};
}
class Emp{
	private byte dept;
	private String name;
	public Emp(String name, byte dept){
		if(dept< Dept.IT || dept> Dept.EEE)
			dept = Dept.IT;
		this.dept = dept;
		this.name = name;
	}
	public float salary(){
		return 2.5f*Dept.bs[dept];
	}
	public void print(){
		System.out.printf("%-10s %-5s Rs %.2f\n", name, Dept.name[dept], salary());
	}
}
class p5{
	public static void main(String args[]){
		new Emp("Srinag", Dept.IT).print();
		new Emp("Skitty S", Dept.CSE).print();
		new Emp("Bubbles", Dept.ECE).print();
	}
}