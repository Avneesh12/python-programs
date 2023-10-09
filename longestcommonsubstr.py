class Solution:
    def lcs(self,n,m,s1,s2):
        dp = [[0]*(m+1) for _ in range(n+1)]
        ans = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(ans,dp[i][j])
        return ans


s = Solution()
print(s.lcs(3,2,"avn","av"))
