import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #字母异位词指字母相同，但排列不同的字符串
        dic1=collections.Counter(s)
        dic2=collections.Counter(t)
        if len(dic1)!=len(dic2):#此种情况直接返回False
            return False
        for key,value in dic2.items():
            if key in dic1 and value==dic1[key]:#key在dic1中并且值相等
                continue
            else:
                return False
        return True

s = "anagram"
t = "nagaram"
so = Solution()
print(so.isAnagram(s,t))
