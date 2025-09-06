class Solution(object):
    def maxProduct(self, nums):
        """
        Author: zhouyuqi
        use Dynamic programming
        the dynamic state is the maxproduct(minpoint) substring which ends with the element i
        """
        if nums is None: return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]

        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i%2, (i-1) %2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])

        return res
    

    '''
    method 1: dynamic programming
    method 2: write 2 for-loops. 1 for-loop iterate each i in the list, 2nd loop finds out the maxpoint substring that begins with element i. 
    '''