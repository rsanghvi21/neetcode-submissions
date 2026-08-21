class Solution {
    public int maxProfit(int[] prices) {

        int left = 0;
        int right = 1;
        int len = prices.length;
        int maxProfit = 0;

        while (right < len){
            if (prices[left] < prices[right]){
                int max = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, max);
                right++;
            }
            else{
                left = right;
                right++;
            }
        }

        return maxProfit;
    }
}
