
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        all_atr = 'abcdefghijklmnopqrstuvwxyz0123456789'
        str_list = []
        for x in s:
            if x in all_atr:
                str_list.append(x)
        if str_list[:] == str_list[::-1]:
            return True
        else:
            return False


so = Solution()
print(so.isPalindrome("A man, a plan, a canal: Panam"))














# new_str = str.lower()
# 将字符串转换为小写
