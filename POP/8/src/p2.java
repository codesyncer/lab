import static java.lang.Thread.sleep;

class RunnableTimer implements Runnable {
    private int time, limit;
    private boolean run;

    RunnableTimer(int time, int limit) {
        this.time = time;
        this.limit = limit;
        run = true;
    }

    public void run() {
        while (run) {
            try {
                sleep(1000);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
            if (time + 1 <= limit)
                time++;
            else
                run = false;
        }
        time = 0;
    }

    void stopTimer() {
        run = false;
    }

    int getTime() {
        return time;
    }
}

public class p2 {

    public static void main(String[] args) {
        RunnableTimer timer1 = new RunnableTimer(0, 50);
        Thread thread1 = new Thread(timer1);
        RunnableTimer timer2 = new RunnableTimer(0, 10);
        Thread thread2 = new Thread(timer2);
        thread1.start();
        thread2.start();
        for (int i = 0; i < 10; i++) {
            System.out.println(timer2.getTime());
            try {
                sleep(2000);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
        timer2.stopTimer();
        timer1.stopTimer();
    }
}
