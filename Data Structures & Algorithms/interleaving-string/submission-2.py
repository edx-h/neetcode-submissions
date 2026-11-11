class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lenS1 = len(s1)
        lenS2 = len(s2)
        dp = [[False for _ in range(lenS2 + 1)] for _ in range(lenS1 + 1)]

        # deal with special cases:
        if len(s3) != (lenS1 + lenS2):
            return False

        # set dp[0][0]
        dp[0][0] = True

        for i in range(lenS1+1):
            for j in range(lenS2+1):
                if i > 0 and s3[i+j-1] == s1[i-1]:
                    # this char is same as s1
                    dp[i][j] = dp[i-1][j]
                
                if dp[i][j] is False and j > 0 and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = dp[i][j-1]
        
        return dp[lenS1][lenS2]