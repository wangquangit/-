import collections


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.Counter(nums)
        for x in dic.values():
            if x == 1:
                return

# 未实现

lst = [1,2,3,4,5,6,7,8,6,7,8,9,0]
so = Solution()
print(so.singleNumber(lst))


print(collections.Counter(lst))