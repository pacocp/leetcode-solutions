class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if count > 0:
                    return count
                else:
                    continue
            elif s[i] != ' ':
                count += 1

        return count 
