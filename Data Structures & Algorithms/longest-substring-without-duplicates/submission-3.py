class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()
        count, l = 0, 0
        for r in range(0, len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            h.add(s[r])
            count = max(count, r - l + 1)
        return count

                

