class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxProfit = 0;
        int len = prices.length;

        while (right < len){
            if (prices[left] < prices[right]){
                if (prices[right] - prices[left] > maxProfit){
                    maxProfit = prices[right] - prices[left];
                }
            }
            else {
                left = right;
            }
            right++;
        }
        return maxProfit;
    }
}
