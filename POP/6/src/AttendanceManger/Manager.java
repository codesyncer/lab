package AttendanceManger;

import java.util.Scanner;

class Student {
    int roll;
    private String name;

    void input(Scanner scan) {
        System.out.print("Name : ");
        name = scan.next();
        System.out.print("Roll : ");
        roll = scan.nextInt();
    }
}

class Class {
    Student[] students;
    private int size;

    Class(int size) {
        this.size = size;
        students = new Student[size];
    }

    Student[] getStudents() {
        return students;
    }

    int classSize() {
        return size;
    }

}

public class Manager {
    private Class myClass = null;

    public Manager() {

    }

    public void buildClass(int n) {
        myClass = new Class(n);
        Scanner scan = new Scanner(System.in);
        for (int i = 0; i < n; ++i) {
            myClass.students[i] = new Student();
            myClass.students[i].input(scan);
        }
    }

    public void takeAttendance() {
        Scanner scan = new Scanner(System.in);
        int count = 0;
        for (Student student : myClass.getStudents()) {
            System.out.print(student.roll + " present? (1/0): ");
            if (scan.nextInt() != 0)
                count++;
        }
        System.out.println("\nPresent: " + 100.0 * count / myClass.classSize() + "%");
    }
}

