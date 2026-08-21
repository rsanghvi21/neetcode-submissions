public class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int temp = left + ((right - left) / 2);
            if (nums[temp] > target) {
                right = temp - 1;
            } else if (nums[temp] < target) {
                left = temp + 1;
            } else {
                return temp;
            }
        }
        return -1;
    }
}