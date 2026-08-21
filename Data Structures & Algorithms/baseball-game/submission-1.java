class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < operations.length; i++){
            String temp = operations[i];

            if (temp.equals("+")){
                int first = stack.pop();
                int second = stack.peek();
                stack.push(first);
                stack.push(first + second);
            } 
            else if (temp.equals("D")){
                int x = stack.peek();
                stack.push(x * 2);
            } 
            else if (temp.equals("C")){
                stack.pop();
            } 
            else {
                int x = Integer.parseInt(temp);
                stack.push(x);
            }
        }

        int sum = 0;
        for (Integer x : stack){
            sum += x;
        }
        
        return sum;        
    }
}