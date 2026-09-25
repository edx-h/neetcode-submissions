class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_vals = []
        for literal in s:
            ascii_vals.append(ord(literal))
        
        sum = 0
        for i in range(len(s)-1):
            sum += abs(ascii_vals[i] - ascii_vals[i+1])
        return sum