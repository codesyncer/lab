class MyTimer extends Timer {
    MyTimer(int start, int limit) {
        super(start, limit);
    }

    void myJoin() {
//        Thread main = Thread.currentThread();
//        System.out.println(Thread.currentThread().getName());
        while (!getState().toString().equals("TERMINATED")) ;
//        Seriously?
    }
}

public class p3 {
    public static void main(String[] args) {
        MyTimer timer1 = new MyTimer(0, 5);
        timer1.start();
//        try {
//            timer1.join();
//        } catch (InterruptedException e) {
//            System.out.println(e.getMessage());
//        }
        timer1.myJoin();
        System.out.println("Hello" + timer1.getState());
    }
}
