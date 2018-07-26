class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_list = [i for i in nums1 if i in nums2]
        return new_list



lst1 = [1]
lst2 = [1,1]
so = Solution()
print(so.intersect(lst1,lst2))