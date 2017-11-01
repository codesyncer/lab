interface Clock {
    void start();

    void stop();

    void update();

    void print();
}

abstract class Pseudo implements Clock {
    public void start() {
    }

    public void stop() {
    }

    public void update() {
    }

    public void print() {
    }
}

class MyClock extends Pseudo {
    private int time;

    public void start() {
        time = 0;
    }

    public void update() {
        time++;
    }

    public void print() {
        System.out.println("Time : " + time);
    }
}

public class p5 {
    public static void main(String arg[]) {
        Clock clock = new MyClock();
        clock.start();
        clock.print();
        clock.update();
        clock.print();
        clock.stop();
        clock.print();
    }
}
