class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_map ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        str_len = len(s)
        sum = 0
        for i in range(0, str_len):
            num = num_map [s[i]]
            sum = sum + num
            if (i != 0 ):
                if num_map[s[i-1]] < num_map[s[i]]:
                    old_num = num_map[s[i-1]]*2
                    sum = sum - old_num
                
        return sum
