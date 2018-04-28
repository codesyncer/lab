class Student{
	static int getTotal(Student student){
		return student.s1+student.s2+student.s3+student.s4+student.s5;
	}
	int s1,s2,s3,s4,s5;
	String roll;
	Student(String roll){
		this.roll = roll;
		s1 = (int)(Math.random()*50+50);
		s2 = (int)(Math.random()*50+50);
		s3 = (int)(Math.random()*50+50);
		s4 = (int)(Math.random()*50+50);
		s5 = (int)(Math.random()*50+50);
	}
	void print(){
		System.out.printf("%-7s\t\t%-5d\t%-5d\t%-5d\t%-5d\t%-5d\n", roll, s1, s2, s3, s4, s5);
	}
}
class p4{
	public static void main(String args[]){
		int n = 7;
		for (int i=0;i<n;++i){
			Student stud = new Student("16IT14"+i);
			stud.print();
			System.out.printf("Total : %d\n", Student.getTotal(stud));
		}
	}
}