class Solution:
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] + nums[y] == target:
                    return [x,y]


lst = [2, 7, 11, 15]
so = Solution()
print(so.twoSum(lst,9))