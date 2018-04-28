package com.company;

class One {
    One() {
        System.out.println("One");
    }
}

class Two {
    Two() {
        System.out.println("Two");
    }
}

class Three {
    Three() {
        System.out.println("Three");
    }
}

class Four {
    Four() {
        System.out.println("Four");
    }
}

class Five extends One {
    Five() {
        System.out.println("Five");
    }
}

class Six extends Five {
    Six() {
        System.out.println("Six");
    }
}


public class Seven extends Six {
    private One b = new One();
    private Two c = new Two();
    private Three l = new Three();

    public void four() {
        System.out.print("Four");
    }

    public static void main(String[] args) {
        new Seven();
    }
}
