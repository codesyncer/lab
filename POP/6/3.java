package AttendanceManger;
class Student{
	int roll;
	String name;
}
class Class{
	Student[] studs;
	int size;
	Class(int size){
		this.size = size;
		studs = new Student[size];
	}
}
class Manager{

}