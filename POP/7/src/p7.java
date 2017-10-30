package es.hol.srinag;

interface Stack {
    class StackException extends Exception {
        StackException(String msg) {
            super(msg);
        }
    }

    void push(int value) throws StackException;

    int pop() throws StackException;

    boolean empty();

    int peek() throws StackException;
}

class ArrayStack implements Stack {
    class ArrayStackException extends StackException {
        ArrayStackException(String msg) {
            super(msg);
        }
    }

    private int maxSize;
    private int array[] = null;
    private int top = -1;

    ArrayStack(int size) {
        maxSize = size;
        array = new int[maxSize];
    }

    ArrayStack() {
        maxSize = 10;
        array = new int[maxSize];
    }

    public void push(int val) throws ArrayStackException {
        if (top >= maxSize - 1 || top < -1)
            throw new ArrayStackException("Overflow");
        top++;
        array[top] = val;
    }

    boolean full() {
        return top >= maxSize - 1;
    }

    public int pop() throws ArrayStackException {
        int val = peek();
        top--;
        return val;
    }

    public boolean empty() {
        return top == -1;
    }

    public int peek() throws ArrayStackException {
        if (top <= -1)
            throw new ArrayStackException("Underflow");
        return array[top];
    }
}

class ListStack implements Stack {
    class listStackException extends StackException {
        listStackException(String msg) {
            super(msg);
        }
    }

    class Node {
        int value;
        Node next;

        Node(int val, Node next) {
            value = val;
            this.next = next;
        }
    }

    private Node head = null;

    public void push(int value) throws listStackException {
        try {
            head = new Node(value, head);
        } catch (OutOfMemoryError e) {
            throw new listStackException(e.getMessage());
        }
    }


    public int pop() throws listStackException {
        int val = peek();
        head = head.next;
        return val;
    }

    public boolean empty() {
        return head == null;
    }

    public int peek() throws listStackException {
        if (head == null)
            throw new listStackException("Underflow");
        return head.value;
    }
}

public class p7 {
    public static void main(String args[]) {
        Stack stack1 = new ArrayStack(5);
        Stack stack2 = new ListStack();
        try {
            for (int i = 0; i < 5; i++)
                stack1.push(i);
            System.out.print("ArrayStack : ");
            for (int i = 0; i < 5; i++)
                System.out.print(stack1.pop() + " ");
            System.out.println();

            for (int i = 0; i < 5; i++)
                stack2.push(i);
            System.out.print("ListStack : ");
            for (int i = 0; i < 5; i++)
                System.out.print(stack2.pop() + " ");

        } catch (Stack.StackException e) {
            System.out.println(e.getMessage());
        }
    }
}
