class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        val = ord(s[0])
        next_val=None
        for i in range(len(s)-1):
            next_val = ord(s[i+1])
            sum += abs(val - next_val)
            val=next_val
        return sum