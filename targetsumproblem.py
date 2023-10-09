# class Solution:
#     def targetsumproblem(self,N,ar,target):
#         SUM = sum(ar)
#         x = SUM+target
#         if x%2 != 0:
#             return 0
#         x = x//2
#         ar.sort(reverse=True)
#         dp = {}
#         def solve(n,sm):
#             item = ar[n-1]
#             if n == 0:
#                 if sm == 0:
#                     return 1
#                 else:
#                     return 0
#             elif (n,sm) in dp:
#                 return dp[(n,sm)]
#             else:
#                 if item <= sm:
#                     c = solve(n-1,sm-item) + solve(n-1,sm)
#                 else:
#                     if sm == 0:
#                         c =  1
#                     else:
#                         c = 0
#                 dp[(n,sm)] = c
#                 return c
#
#
#         return solve(N,x)
#
# s = Solution()
# print(s.targetsumproblem(5,[1,1,1,1,1],3))












# class Solution:
#     def targetsumproblem(self,N,ar,target):
#         SUM = sum(ar)
#         x = SUM + target
#         if x%2 != 0:
#             return 0
#         x = x//2
#         ar.sort(reverse=True)
#         dp = [[0]*(SUM+1) for i in range(N)]
#         for i in range(N):
#             for j in range(SUM+1):
#                 sm = j
#                 item = ar[i]
#                 if i == 0:
#                     if sm == 0:
#                         if item == 0:
#                             dp[i][j] =  2
#                         else:
#                             dp[i][j] =  1
#                     else:
#                         if sm == item:
#                             dp[i][j] =  1
#                 else:
#                     if item <= sm:
#                         dp[i][j] = dp[i-1][sm-item] + dp[i-1][sm]
#                     else:
#                         dp[i][j] = dp[i-1][sm]
#         return dp[N-1][x]
#
#
#
# s = Solution()
# print(s.targetsumproblem(5,[1,1,1,1,1,1],3))
#











