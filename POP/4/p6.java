class Shape{
	float a,b;
	float area;
	static final byte SQUARE = 0;
	static final byte CUBE = 1;
	static final byte SPHERE = 2;
	static final byte RECT = 3;
	static final byte CYN = 4;
	static final float pi = 3.14159f;
	Shape(){
		a=b=0;
	}
	Shape(float a){
		this.a = a;
		area = a*a;
	}
	Shape(float a, float b){
		this.a = a;
		this.b = b;
		area = a*b;
	}
	Shape(float a, byte type){
		this.a = a;
		switch(type){
			case Shape.SQUARE:
				area = a*a;
				break;
			case Shape.CUBE:
				area = 6*a*a;
				break;
			case Shape.SPHERE:
				area = 4*pi*a*a;
				break;	
		}
	}
	Shape(float a, float b, byte type){
		this.a = a;
		this.b = b;
		switch(type){
			case Shape.RECT:
				area = a*b;
				break;
			case Shape.CYN:
				area = 2*pi*(a*a+a*b);
				break;
		}
	}
	float getArea(){
		return area; 
	}
}
class p6{
	public static void main(String args[]){
		System.out.printf("Area of square of side 2cm : %.2f cmsq\n", new Shape(2).getArea());		
		System.out.printf("Area of cube of side 2cm : %.2f cmsq\n", new Shape(2,Shape.CUBE).getArea());		
		System.out.printf("Area of rectangle of sides 2cm and 3cm : %.2f cmsq\n", new Shape(2,3).getArea());		
		System.out.printf("Area of sphere of radius 2cm : %.2f cmsq\n", new Shape(2, Shape.SPHERE).getArea());		
		System.out.printf("Area of cylinder of radius 2cm and height 3cm: %.2f cmsq\n", new Shape(2,3,Shape.CYN).getArea());		
	}
}