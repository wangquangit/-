class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        now_x = str(x)
        new_x = []
        new_x_two = []
        for x in now_x:
            if x == '-':
                new_x.append('-')
            else:
                new_x_two.insert(0,x)
        return int(''.join(new_x + new_x_two))

so = Solution()
print(so.reverse(-3450))