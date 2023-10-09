# class Solution:
#     def unboundknapsack(self,N,W,wt,val):
#         dp = {}
#         def solve(n,cap):
#             cw = wt[n-1]
#             cv = val[n-1]
#             if n == 0 or cap == 0:
#                 return 0
#             elif (n,cap) in dp:
#                 return dp[(n,cap)]
#             else:
#                 if cw <= cap:
#                     c1 = cv + solve(n,cap-cw)
#                     c2 = solve(n-1,cap)
#                     c = max(c1,c2)
#                 else:
#                     c = solve(n-1,cap)
#                 dp[(n,cap)] = c
#                 return c
#
#         return solve(N,W)
#
# s = Solution()
# print(s.unboundknapsack(2,3,[2,1],[1,1]))










class Solution:
    def unboundknapsack(self,N,W,wt,val):
        dp = [[0]*(W+1) for _ in range(N)]
        for i in range(N):
            for j in range(W+1):
                cap = j
                cv = val[i]
                cwt = wt[i]
                if i == 0:
                    dp[i][j] = (cap//cwt)*cv
                else:
                    if cwt <= cap:
                        c1 = cv + dp[i][cap-cwt]
                        c2 = dp[i-1][cap]
                        c = max(c1,c2)
                    else:
                        c = dp[i-1][cap]
                    dp[i][j] = c
        return dp[N-1][W]

s = Solution()
print(s.unboundknapsack(2,3,[2,1],[1,1]))













