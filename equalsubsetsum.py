# class Solution:
#     def equalsubsetsum(self,N,ar):
#         sm = sum(ar)
#         if sm%2 != 0:
#             return 0
#         sm1 = sm//2
#         ar.sort(reverse=True)
#         def solve(n,sm1):
#             if sm1 == 0:
#                 return 1
#             elif n == 0:
#                 return 0
#             else:
#                 item = ar[n-1]
#                 if item <= sm1:
#                     c1 = solve(n-1,sm1-item)
#                     c2 = solve(n-1,sm1)
#                     c = c1 or c2
#                 else:
#                     c = 0
#                 return c
#
#         return solve(N,sm1)
#
# s = Solution()
#
# print(s.equalsubsetsum(4,[1,2,3,7]))










class Solution:
    def equalsubsetsum(self,N,ar):
        sm = sum(ar)
        if sm%2 != 0:
            return 0
        smm = sm//2
        dp = [[0]*(smm+1) for _ in range(N)]
        for i in range(N):
            for j in range(smm+1):
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
        return dp[N-1][smm]

s = Solution()
print(s.equalsubsetsum(4,[1,2,3,5]))












