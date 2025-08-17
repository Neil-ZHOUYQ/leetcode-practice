class Solution(object):
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n
       
        F=[0]*(n+1)
        F[1] = 1
        F[2] = 2

        i = 3
        while i <= n:       
            F[i] = F[i-1] + F[i-2]
            i+=1
    
        return F[n]
