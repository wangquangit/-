

class Solution:
    def myAtoi(self,s):
        import re
        list_s = re.findall(r"^[-+]?\d+", s.strip())
        print(list_s)
        if not list_s:
            return 0
        return int(''.join(list_s))







so = Solution()
print (so.myAtoi('-124324 32424'))