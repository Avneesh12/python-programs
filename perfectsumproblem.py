# class Solution:
#     def perfectsum(self,N,ar,sm):
#         def solve(n,sm1):
#             if n == 0:
#                 if sm1 == 0:
#                     return 1
#                 else:
#                     return 0
#             else:
#                 item = ar[n-1]
#                 if item <= sm1:
#                     c = solve(n-1,sm1-item) + solve(n-1,sm1)
#                 else:
#                     if sm1 == 0:
#                         c = 1
#                     else:
#                         c = 0
#                 return c
#         return solve(N,sm)
#
# s = Solution()
# print(s.perfectsum(4,[1,2,3,4],0))




# class Solution:
#     def perfectsumproblem(self,N,ar,sm):
#         dp = {}
#         def solve(n,sm1):
#             if n == 0:
#                 if sm1 == 0:
#                     return 1
#                 else:
#                     return 0
#             elif (n,sm1) in dp:
#                 return dp[(n,sm1)]
#             else:
#                 item = ar[n-1]
#                 if item <= sm1:
#                     c = solve(n-1,sm1-item) + solve(n-1,sm1)
#                 else:
#                     if sm1 == 0:
#                         c = 1
#                     else:
#                         c = 0
#                 dp[(n,sm1)] = c
#                 return c
#         return solve(N,sm)
#
# s = Solution()
# print(s.perfectsumproblem(4,[1,2,3,4],6))



#
# class Solution:
#     def perfectsumproblem(self,N,ar,sm):
#         d = [[0]*(sm+1) for _ in range(N)]
#         for i in range(N):
#             for j in range(sm+1):
#                 item = ar[i]
#                 sm1 = j
#                 if i == 0:
#                     if sm1 == 0:
#                         if item == 0:
#                             d[i][j] = 2
#                         else:
#                             d[i][j] = 1
#                     else :
#                         if sm1 == item:
#                             d[i][j] = 1
#                 else:
#                     if item <= sm1:
#                         d[i][j] = d[i-1][sm1-item] + d[i-1][sm1]
#                     else:
#                         d[i][j] = d[i-1][sm1]
#         return d[N-1][sm]
#
# s = Solution()
# print(s.perfectsumproblem(4,[1,2,3,4],3))
#















