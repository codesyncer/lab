package es.hol.srinag;

import java.util.Scanner;

class myException extends Exception {
    myException(String msg) {
        super(msg);
    }
}

public class p6 {
    private static double calc(int i, int j) throws myException {
        if (j == 0)
            throw new myException("Second param cannot be zero");
        if (i < 0)
            throw new myException("First param is negative");
        return Math.pow(i, 0.5) / j;
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter two integers : ");
        try {
            int i = in.nextInt(), j = in.nextInt();
            System.out.printf("sqrt %d / %d = %f", i, j, calc(i, j));
        } catch (myException e) {
            System.out.println(e.getMessage());
        }
    }
}
