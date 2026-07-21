from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for s in strs:
            x += str(len(s)) + "#" + s
        return x

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            output.append(s[start:end])
            i = end
            
        return output