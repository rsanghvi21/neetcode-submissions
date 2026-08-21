class Solution {
    public int removeDuplicates(int[] nums) {
        List<Integer> s = new ArrayList<>();
        int count = 0;
        for (int i = 0; i < nums.length; i++){
            if (!s.contains(nums[i])){
                s.add(nums[i]);
                count++;
            }
        }
        int i = 0;
        for (Integer x : s){
            nums[i++] = x;
        }

        return count;
    }
}