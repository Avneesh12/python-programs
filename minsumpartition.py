# class Solution:
#     def minsumpartition(self,N,ar):
#         SUM = sum(ar)
#         p1 = SUM
#         dp = {}
#         def solve(n,p1,SUM):
#             p2 = SUM - p1
#             item = ar[n-1]
#             if n== 0:
#                  return p1-p2
#             elif (n,p1,SUM) in dp:
#                 return dp[(n,p1,SUM)]
#             else:
#                 if p1 - item >= p2 + item:
#                     c1 = solve(n-1,p1-item,SUM)
#                     c2 = solve(n-1,p1,SUM)
#                     c = min(c1,c2)
#                 else:
#                     c = solve(n-1,p1,SUM)
#                 dp[(n,p1,SUM)] = c
#                 return c
#         return solve(N,SUM,SUM)
#
# s = Solution()
# print(s.minsumpartition(4,[1,6,11,5]))




# class Solution:
#     def minimumpartitionsum(self,N,ar):
#         SUM = sum(ar)
#         dp = [[0]*(SUM+1) for _ in range(N)]
#         for i in range(N):
#             for j in range(SUM+1):
#                 item = ar[i]
#                 sm = j
#                 if i == 0:
#                     if sm == 0 or sm == item:
#                         dp[i][j] = 1
#                     else:
#                         dp[i][j] = 0
#                 else:
#                     if item <= sm:
#                         c = dp[i-1][sm-item] or dp[i-1][sm]
#                     else:
#                         c = dp[i-1][sm]
#                     dp[i][j] = c
#         ans = SUM
#
#         for j in range(SUM+1):
#             if dp[N-1][j] == 1:
#                 # p1 = j
#                 # p2 = SUM -p1
#                 # diff = abs(p1-p2)
#                 # ans = min(diff,ans)
#                 ans = min(ans,abs(SUM-2*j))
#         return ans
#
#
#
#
#
#
# s = Solution()
# print(s.minimumpartitionsum(3,[1,2,0]))
#












