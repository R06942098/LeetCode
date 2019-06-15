class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ### 只要有一個即為過關
        
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]

        low = 0
        high = len(s) - 1

        while low < high:
            ### that's similar to construct binary search tree..
            if s[low] != s[high]:
                return isPalindrome(strPart(s, low)) or isPalindrome(strPart(s, high))
            low += 1
            high -= 1
        return True
        """


        for i in range(int(len(s)/2)):
            temp = s[:i] + s[i+1:]
            temp_1 = s[:len(n)-i] + s[len(n)-i+1:]

            if temp == temp[::-1] or temp_1 == temp[::-1]:
                return True

        return True
        """