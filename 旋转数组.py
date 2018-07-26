class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for x in range(k):
            nums.insert(0,nums.pop(-1))

        return nums

so = Solution()
print(so.rotate([1,2,3,4,5,6,7],3))