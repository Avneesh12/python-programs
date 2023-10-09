# class Solution:
#     def rodcutting(self,N,price):
#         dp = {}
#         def solve(cl,rl):
#             if cl == 0 or rl == 0:
#                 return 0
#             elif (cl,rl) in dp:
#                 return dp[(cl,rl)]
#             else:
#                 cv = price[cl-1]
#                 if cl <= rl:
#                     c = max(cv+solve(cl,rl-cl) , solve(cl-1,rl))
#                 else:
#                     c = solve(cl-1,rl)
#                 dp[(cl,rl)] = c
#                 return c
#         return solve(N,N)
#
# s = Solution()
# print(s.rodcutting(8,[1,5,8,9,10,17,17,20]))






class Solution:
    def rodcuttng(self,N,price):
        dp = [[0]*(N+1) for _ in range(N+1)]
        for i in range(N+1):
            for j in range(N+1):
                cl = i
                rl = j
                if cl == 0 or rl == 0:
                    dp[i][j] = 0
                else:
                    if cl<= rl:
                        val = price[cl-1]
                        c = max(val+dp[cl][rl-cl] , dp[cl-1][rl])
                    else:
                        c = dp[cl-1][rl]
                    dp[i][j] = c
        return dp[N][N]

s = Solution()
print(s.rodcuttng(8,[1,5,8,9,10,17,17,20]))















