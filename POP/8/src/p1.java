class Timer extends Thread {
    private int time, limit;
    private boolean run;

    Timer(int time, int limit) {
        this.time = time;
        this.limit = limit;
    }

    public void start() {
        run = true;
        super.start();
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

public class p1 {

    public static void main(String[] args) {
        Timer timer1 = new Timer(0, 50);
        Timer timer2 = new Timer(0, 10);
        timer1.start();
        timer2.start();
        for (int i = 0; i < 10; i++) {
            System.out.println(timer2.getTime());
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
        timer2.stopTimer();
        timer1.stopTimer();
    }
}
