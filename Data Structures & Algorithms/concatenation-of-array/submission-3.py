class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        newList = [0] * (2 * length)   
        
        for i in range(length):
            newList[i] = nums[i]             
            newList[i + length] = nums[i]    
        
        return newList
