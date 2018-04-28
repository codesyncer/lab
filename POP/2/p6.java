import java.util.Scanner;
class VCal{
	final float pi = 3.14159f;
	public static final byte CONE = 0;
	public static final byte CYLINDER = 1;
	public float volume(float a){
		return a*a*a;
	}
	public float volume(float l, float b, float h){
		return l*b*h;
	}
	public float volume(float r, float h, byte obj){
		if(obj == CONE)
			return pi*r*r*h/3f;
		if(obj == CYLINDER)
			return pi*r*r*h;
		return -1;
	}
}
class p6{
	public static void main(String args[]){
		VCal calc = new VCal();
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter length of side of cube in cm : ");
		System.out.println("Volume of cube = "+calc.volume(scan.nextFloat())+" cubiccm");
		System.out.print("Enter length of sides of cuboid in cm : ");
		System.out.println("Volume of cuboid = "+calc.volume(scan.nextFloat(), scan.nextFloat(), scan.nextFloat())+" cubiccm");
		System.out.print("Enter radius and height of cylinder in cm : ");
		System.out.println("Volume of cylinder = "+calc.volume(scan.nextFloat(), scan.nextFloat(), VCal.CYLINDER)+" cubiccm");
		System.out.print("Enter length of sides of box in cm : ");
		System.out.println("Volume of cuboid = "+calc.volume(scan.nextFloat(), scan.nextFloat(), scan.nextFloat())+" cubiccm");
		System.out.print("Enter radius and height of cone in cm : ");
		System.out.println("Volume of cone = "+calc.volume(scan.nextFloat(), scan.nextFloat(), VCal.CONE)+" cubiccm");
	}
}