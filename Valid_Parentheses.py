'''
class Solution:
    this method has too many assumpytion .. 
    def isValid(self, s) :
        left = ['(','{','[']
        right = [')','}',']']
        if len(s)%2 !=0 : 
            return False 
        i=0
        while i < len(s): 
            if s[i] in left:
                ind = left.index(s[i])
                if s[i+1] == right[0]: 
                    i += 2 
                else: 
                    start = i 
                    temp =  (s[i:].find(right[left.index(s[i])]))
                    qq = list(s[i:]).count(right[left.index(s[i])])
                    print(qq)
                    if temp == -1: 
                        return False
                    else :      
                        end =  i + temp 
                    temp_1 = s[i:end+1]

                    if len(temp_1)%2 !=0 :
                        return False 
                    else:
                        while i < end: 
                            if s[i] == s[i+1]:
                                i += 2 
                            else :  
                                temp_2 = s[i:end+1]
                                mid_point = int(len(temp_2)/2)
                                for k in range(mid_point):
                                    if temp_2[k] in left :
                                        lef = left.index(temp_2[k])
                                        if temp_2[len(temp_2)-k-1] in right:
                                            rig = right.index(temp_2[len(temp_2)-k-1])
                                        else:
                                            return False
                                        if lef == rig:
                                            pass
                                        else :
                                            return False 
                                    else:
                                        return False
                                i += len(temp_2)
            else:
                return False
        return True 
'''


class Solution(object):
    ### need to learn it and solve this problem.
    ### First in Fisrt out, that is the concept of stack..
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            print(stack)
            if not stack:
                stack.append(c)
            else:
                if c in ['(', '[', '{']:
                    stack.append(c)
                else:
                    top = stack.pop()
                    if (top == '(' and c != ')') or \
                        (top == '[' and c != ']') or \
                        (top == '{' and c != '}'):
                        return False
        #return not stack
        return True

a = "(([])){})"
a = "(])]"
#a = "({()})()"
b= Solution()
print(b.isValid(a))

                