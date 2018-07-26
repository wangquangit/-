class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ss = 0
        for x in range(len(prices)):
            try:
                if prices[x] < prices[x+1]:
                    ss += prices[x+1] - prices[x]
            except:
                pass
        return ss



lst = [1,2,3,4,5]

so = Solution()
print(so.maxProfit(lst))