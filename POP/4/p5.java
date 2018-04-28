class Outer{
	class Inner{
		void foo(){
			System.out.println("Inner");
		}
		void callBar(){
			bar();
		}
	}
	static class Sinner{
		void foo(){
			System.out.println("Sinner");
		}
		// void callBar(){
		// 	bar();
		// }
	}
	void bar(){
		System.out.println("Outer");
	}
	Inner obji = new Inner();
}
class p5{
	public static void main(String args[]){
		Outer objo = new Outer();
		objo.bar();
		objo.obji.foo();
		objo.obji.callBar();
		Outer.Sinner obj = new Outer.Sinner();
		obj.foo();
	}
}