class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] > nums[y]:
                    nums[x],nums[y] = nums[y],nums[x]
        print(nums)
        for z in range(len(nums)):# 未实现
            try:
                if nums[z] == nums[z+1]:
                    del nums[z]
            except:
                pass
        return nums

so = Solution()
print(so.removeDuplicates([3,1,3,2,3,5,4,3,6,7,3]))

