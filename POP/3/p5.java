import java.util.Scanner;
class ACal{
	final float pi = 3.14159f;
	public static final byte CONE = 0;
	public static final byte CYLINDER = 1;
	public static final byte PRISM = 2;
	public static final byte PYRAMID = 3;
	public float area(float r){
		return 3*pi*r*r;
	}
	public float area(float l, float w, float h, byte obj){
		if(obj == PRISM)
			return 2*(l*w + w*h + h*l);
		if(obj == PYRAMID)
			return (float)(l*w + l*Math.sqrt((w/2)*(w/2)+h*h) + w*Math.sqrt((l/2)*(l/2) + h*h));
		return -1;
	}
	public float area(float r, float h, byte obj){
		if(obj == CONE)
			return (float)(pi*r*(r + Math.sqrt(h*h + r*r)));
		if(obj == CYLINDER)
			return 2*pi*r*(r+h);
		return -1;
	}
}
class p5{
	public static void main(String args[]){
		ACal calc = new ACal();
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter radius and height of cone in cm : ");
		System.out.println("Area of cone = "+calc.area(scan.nextFloat(), scan.nextFloat(), ACal.CONE)+" sqcm");
		System.out.print("Enter radius and height of cylinder in cm : ");
		System.out.println("Area of cylinder = "+calc.area(scan.nextFloat(), scan.nextFloat(), ACal.CYLINDER)+" sqcm");
		System.out.print("Enter length of sides of rectangular prism in cm : ");
		System.out.println("Area of prism = "+calc.area(scan.nextFloat(), scan.nextFloat(), scan.nextFloat(), ACal.PRISM)+" sqcm");
		System.out.print("Enter length of sides of base and height of pyramid in cm : ");
		System.out.println("Area of pyramid = "+calc.area(scan.nextFloat(), scan.nextFloat(), scan.nextFloat(), ACal.PYRAMID)+" sqcm");
		System.out.print("Enter radius of hemisphere in cm : ");
		System.out.println("Area of hemisphere = "+calc.area(scan.nextFloat())+" sqcm");		
	}
}