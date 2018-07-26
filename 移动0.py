class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        s = -1
        for x in nums:
            s += 1
            print(s)
            if x == 0:
                nums.append(nums.pop(s))
        return nums

lst = [0,0,0,0,7,0,0,8,5,0,4,5,7]


so = Solution()
print(so.moveZeroes(lst))