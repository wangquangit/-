class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ints = ' -0123456789'
        new_str_list = []
        if str == '':
            return 0
        if str == '-':
            return '-'
        if str[0] not in ints:
            return 0
        for x in str:
            if x in ints:
                new_str_list.append(x)
        return int(''.join(new_str_list))


str = "words and 987"
str = "4193 with words"
str = "-91283472332"
str = '-'
so = Solution()
print(so.myAtoi(str))