class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int maxCount = 0;
        int majority = nums[0];

        for (int i = 0; i < nums.length; i++){
            if (!map.containsKey(nums[i])){
                map.put(nums[i], 1);
            }
            else{
                int x = map.get(nums[i]);
                x++;
                map.put(nums[i], x);
            }

            if (map.get(nums[i]) > maxCount){
                maxCount = map.get(nums[i]);
                majority = nums[i];
            }
        }
        return majority;
    }
}