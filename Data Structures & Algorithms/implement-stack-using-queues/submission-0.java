public class MyStack {
    private Queue<Integer> left;
    private Queue<Integer> right;

    public MyStack() {
        left = new LinkedList<>();
        right = new LinkedList<>();
    }

    public void push(int x) {
        right.offer(x);
        while (!left.isEmpty()) {
            right.offer(left.poll());
        }
        Queue<Integer> temp = left;
        left = right;
        right = temp;
    }

    public int pop() {
        return left.poll();
    }

    public int top() {
        return left.peek();
    }

    public boolean empty() {
        return left.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */