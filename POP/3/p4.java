import java.util.Scanner;
class p4{
	static class Student{
		int aroll, sem;
		String name, roll;
		Student(int aroll, int sem, String name, String roll){
			this.aroll = aroll;
			this.sem = sem;
			this.name = name;
			this.roll = roll;
		}
	}

	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.print("Number of students : ");
		int n = scan.nextInt();
		Student[] students = new Student[n];
		int aroll, sem;
		String name, roll;
		for(int i=0; i<n; ++i){
			System.out.print("Name : ");
			name = scan.next();
			System.out.print("Roll : ");
			roll = scan.next();
			System.out.print("Admission number : ");
			aroll = scan.nextInt();
			System.out.print("Semester : ");
			sem = scan.nextInt();
			students[i] = new Student(aroll, sem, name, roll);
		}
		System.out.printf("%-10s\t%-7s\t%s\t%s\n","Name", "Roll#", "Admission#", "Sem");
		for(int i=0; i<n; ++i)
			System.out.printf("%-10s\t%s\t%-10d\t%-3d\n",students[i].name, students[i].roll, students[i].aroll, students[i].sem);
	}
}
