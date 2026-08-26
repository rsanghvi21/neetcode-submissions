class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for words in strs:
            s += str(len(words)) + "$" + words
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        
        index = 0
        while index < len(s):
            j = index
            while s[j] != "$":
                j += 1
            length_of_word = int(s[index:j])
            start = j + 1
            end = start + length_of_word
            result.append(str(s[start:end]))
            index = end
        return result
