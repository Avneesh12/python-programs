# class Solution:
#     def lcs(self,x,y,str1,str2):
#         dp = {}
#         def solve(n,m,s1,s2):
#             if n == 0 or m == 0:
#                 return 0
#             elif (n,m) in dp:
#                 return dp[(n,m)]
#             else:
#                 if s1[n-1] == s2[m-1]:
#                     c = 1 + solve(n-1,m-1,s1,s2)
#                 else:
#                     c1 = solve(n-1,m,s1,s2)
#                     c2 = solve(n,m-1,s1,s2)
#                     c = max(c1,c2)
#                 dp[(n,m)] = c
#                 return c
#         return solve(x,y,str1,str2)
#
# s = Solution()
# print(s.lcs(6,6,"ABCDGH","AEDFHR"))






























