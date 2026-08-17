class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        x = set()
        index = 0
        result = 0

        for i in range(len(s)):
            while s[i] in x:
                x.remove(s[index])
                index += 1
            x.add(s[i])
            result = max(result, i - index + 1)
        return result
        