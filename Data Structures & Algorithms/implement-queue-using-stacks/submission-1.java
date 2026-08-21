class MyQueue {

    private Stack<Integer> left;
    private Stack<Integer> right;

    public MyQueue() {
        left = new Stack<Integer>();
        right = new Stack<Integer>();
    }
    
    public void push(int x) {
        left.push(x);
    }
    
    public int pop() {
        while (left.size() > 1) {
            right.push(left.pop());
        }
        int result = left.pop();
        while (!right.isEmpty()) {
            left.push(right.pop());
        }
        return result;
    }
    
    public int peek() {
        while (left.size() > 1) {
            right.push(left.pop());
        }
        int result = left.peek();
        while (!right.isEmpty()) {
            left.push(right.pop());
        }
        return result;
    }
    
    public boolean empty() {
        return left.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */