class Solution:
    def lcs(self,ar1,ar2):
        n = len(ar1)
        m = len(ar2)
        dp =  [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if ar1[i-1] == ar2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        ans = []
        i,j = n,m
        while i>0 and j> 0:
            if ar1[i-1] == ar2[j-1]:
                ans.append(ar2[j-1])
                j -= 1
                i -= 1
            else:
                if dp[i-1][j] >= dp[i][j-1]:
                    i -= 1
                else:
                    j -=1
        return ans[::-1]

s = Solution()
print(s.lcs([1,2,3,4,1],[3,4,1,2,1,3]))

