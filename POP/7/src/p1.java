import java.io.File;
import java.io.IOException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class p1 {

    public static void main(String[] args) {
        Scanner scan = null;
        int i, j;
        File file = new File("ip.dat");
        try {
            scan = new Scanner(file);
            i = scan.nextInt();
            j = scan.nextInt();
            System.out.println(i / j);
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic Exception : " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO Exception : " + e.getMessage());
        } catch (NoSuchElementException e) {
            System.out.println("Found less than 2 elements");
        } finally {
            if (scan != null)
                scan.close();
        }
    }
}