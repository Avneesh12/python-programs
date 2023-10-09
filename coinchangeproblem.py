class Solution:
    def coinchangeproblem(self,N,ar,amount):
        dp = {}
        ar.sort(reverse=True)
        def solve(n,amt):
            if n == 0:
                if amt == 0:
                    return 1
                else:
                    return 0
            elif (n,amt) in dp:
                return dp[(n,amt)]
            else:
                coin = ar[n-1]
                if coin <= amt:
                    c1 = solve(n,amt-coin)
                    c2 = solve(n-1,amt)
                    c = c1 + c2
                else:
                    if amt == 0:
                        c = 1
                    else:
                        c = 0
            dp[(n,amt)] = c
            return c

        return solve(N,amount)

s = Solution()
print(s.coinchangeproblem(3,[1,2,3],4))