class Solution:
	#def compress(self, chars: List[str]) -> int:
	def compress(self, chars): 
		## for example : 
		## Input: ["a","a","b","b","c","c","c"]
		## Output: ["a","2","b","2","c","3"]
		#chars.sort()
		if len(chars) == 0 :
			return [] 
		'''
		I think this must modify by change the list content (that's called in-place)...
		temp = []
		for i in chars: 
			if i not in temp: 
				temp.append(i)

		for i in temp: 
			start = chars.index(i)
			nums = chars.count(i)
			if nums == 1 : 
				w_list = [i]
			else: 
				temp = str(nums)
				if len(temp) == 1 :
					w_list = [i, str(nums)]
				else: 
					w_list = [i]
					for i in temp: 
						w_list.append(i)
			chars[start:start+nums] = w_list
		return chars
		'''
		i = 0 
		le = len(chars)
		while i < le: 
			a = chars[i]
			count = 1
			while True : 
				if i + count > len(chars)-1:
					break
				if chars[i+count] != a : 
					break
				else:
					count += 1 

			if count == 1 :
				w_list = [a]
			else: 
				temp = str(count)
				if len(temp) == 1 : 
					w_list = [a, temp]
				else: 
					w_list = [a]
					for q in temp: 
						w_list.append(q)
			chars[i:i+count] = w_list
			le = len(chars)
			i += len(w_list)
		return chars
b = Solution()
#a = ["a","a","b","b","c","c","c",'a','a']
#a = ['a']
#a = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
a = ["a","a","b","b","c","c","c"]
print(b.compress(a))

