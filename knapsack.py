# class Solution:
#     def knapsack(self,N,W,wt,val):
#         def solve(n,cap):
#             if n == 0 or cap == 0:
#                 return 0
#             else:
#                 cwt = wt[n-1]
#                 cv = val[n-1]
#                 if cwt <= cap:
#                     c1 = cv + solve(n-1,cap-cwt)
#                     c2 = solve(n-1,cap)
#                     c = max(c1,c2)
#                 else:
#                     c = solve(n-1,cap)
#                 return c
#         return solve(N,W)
#
#
# s = Solution()
# print(s.knapsack(3,4,[1,2,3],[4,5,1]))






#
# class Solution:
#     def knapsack(self,N,W,wt,val):
#         dp = {}
#         def solve(n,cap):
#             if n == 0 or cap==0:
#                 return 0
#             elif (n,cap) in dp:
#                 return dp[(n,cap)]
#             else:
#                 cwt = wt[n-1]
#                 cv = val[n-1]
#                 if cwt <= cap:
#                     c1 = cv + solve(n-1,cap-cwt)
#                     c2 = solve(n-1,cap)
#                     c = max(c1,c2)
#                 else:
#                     c = solve(n-1,cap)
#                 dp[(n,cap)] = c
#                 return c
#         return solve(N,W)
#
#
# s = Solution()
# print(s.knapsack(3,4,[1,2,3],[4,5,1]))
#







class Solution:
    def knapsack(self,N,W,wt,val):
        dp = [[0]*(W+1) for i in range(N)]
        for i in range(N):
            for j in range(W+1):
                cwt = wt[i]
                cv = val[i]
                cap = j
                if i == 0:
                    if cwt <= cap:
                        dp[i][j] = cv
                    else:
                        dp[i][j] = 0
                else:
                    if cwt <= cap:
                        c1 = cv + dp[i-1][cap-cwt]
                        c2 = dp[i-1][cap]
                        c = max(c1,c2)
                    else:
                        c = dp[i-1][cap]
                    dp[i][j] = c
        return dp[N-1][W]

s = Solution()
print(s.knapsack(3,4,[1,2,3],[4,5,1]))














