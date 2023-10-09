# class Solution:
#     def subsetsum(self,N,ar,sm):
#         ar.sort(reverse=True)
#         def solve(n,sm1):
#             item = ar[n-1]
#             if sm1 == 0:
#                 return 1
#             elif n == 0:
#                 return 0
#             else:
#                 if item <= sm1:
#                     c1 = solve(n-1,sm1-item)
#                     c2 = solve(n-1,sm1)
#                     c = c1 or c2
#                 else:
#                     c = 0
#                 return c
#
#         return solve(N,sm)
#
# s = Solution()
# print(s.subsetsum(3,[1,2,3],0))
#
#














# class Solution:
#     def subsetsum(self,N,ar,sm):
#         d = {}
#         def solve(n,sm1):
#             if sm1 == 0:
#                 return 1
#             elif n == 0:
#                 return 0
#             elif (n,sm1) in d:
#                 return d[(n,sm1)]
#             else:
#                 item = ar[n-1]
#                 if item <= sm1:
#                     c1 = solve(n-1,sm1-item)
#                     c2 = solve(n-1,sm1)
#                     c = c1 or c2
#                 else:
#                     c = solve(n-1,sm1)
#                 d[(n,sm1)] = c
#                 return c
#         return solve(N,sm)
#
# s = Solution()
# print(s.subsetsum(3,[1,2,3]))




class Solution:
    def subsetsum(self,N,ar,sm):
        dp = [[0]*(sm+1) for _ in range(N)]
        for i in range(N):
            for j in range(sm+1):
                sm1 = j
                item = ar[i]
                if i == 0:
                    if sm1 == 0 or sm1 == item:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:
                    if item <= sm1:
                        c1 = dp[i-1][sm1-item]
                        c2 = dp[i-1][sm1]
                        c = c1 or c2
                    else:
                        c = dp[i-1][sm1]
                    dp[i][j] = c
        return [dp[N-1][sm],dp]


s = Solution()
print(s.subsetsum(3,[1,2,3],0))
















