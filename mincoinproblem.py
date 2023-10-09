# class Solution:
#     def coinproblem(self,ar,amount):
#         N = len(ar)
#         dp = {}
#         ar.sort(reverse=True)
#         def solve(n,amt):
#             if amt == 0:
#                 return 0
#             elif n == 0:
#                 return float('INF')
#             elif (n,amt) in dp:
#                 return dp[(n,amt)]
#             else:
#                 val = ar[n-1]
#                 if val <= amt:
#                     c = min(1+solve(n,amt-val) , solve(n-1,amt))
#                 else:
#                     c = float('INF')
#                 dp[(n,amt)] = c
#                 return c
#
#         ans = solve(N,amount)
#         if ans >= 10**9+7:
#             return -1
#         else:
#             return ans
#
# s = Solution()
# print(s.coinproblem([1,2,5],11))








# class Solution:
#     def coinproblem(self,arr,amount):
#         dp = {}
#         arr.sort()
#         def solve(amt):
#             if amt == 0:
#                 return 0
#             elif amt in dp:
#                 return dp[amt]
#             else:
#                 ans = float('INF')
#                 for coin in arr:
#                     if coin <= amt:
#                         ans = min(1+solve(amt-coin),ans)
#                     else:
#                         break
#                 dp[amt] = ans
#                 return ans
#         val = solve(amount)
#         if val >= 10**9+7:
#             return -1
#         else:
#             return val
#
# s = Solution()
# print(s.coinproblem([1,2,5],11))




class Solution:
    def coinproblem(self,arr,amount):
        arr.sort()
        dp = [[0]*(amount+1)]
        for amt in range(1,amount+1):
            ans = float('INF')
            for coin in arr:
                if coin <= amt:
                    c = 1+dp[amt-coin]
                    ans = min(ans,c)
                else:
                    break
            dp[amt] = ans
        if dp[amount] >= 10**9+7:
            return -1
        else:
            return dp[amount]

s = Solution()
print(s.coinproblem([1,2,5],11))


























