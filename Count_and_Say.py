class Solution:
	#def countAndSay(self, n: int) -> str:
	'''
	1.     1 
	2.     11 See it and say there is one digit one.
	3.     21 See it and say there is two digit one.
	4.     1211 See it and say there is one digit two and one digit one.
	5.     111221 See it and say there is one digits on, one digit two and two digit one.
	'''
	def countAndSay(self, n):

		for i in range(n):
			if i == 0 : 
				#res = self.compress('1')
				res = '1'
				print(res)
			else: 
				res = self.compress(res)
				print(res)
		return res 
	'''
	This is really helpful.
	def toStr(self, a):
		return ''.join(a)
	'''
	def compress(self, chars): 
		## for example : 
		## Input: ["a","a","b","b","c","c","c"]
		## Output: ["a","2","b","2","c","3"]
		#chars.sort()
		chars = list(chars)
		if len(chars) == 0 :
			return [] 
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
				w_list = ['1', a]
			else: 
				temp = str(count)
				if len(temp) == 1 : 
					w_list = [temp, a]
				else: 
					w_list = []
					for q in temp: 
						w_list.append(q)
					w_list.append(a)
			chars[i:i+count] = w_list
			le = len(chars)
			i += len(w_list)
		return ''.join(chars)

b = Solution()
a = 5
print(b.countAndSay(a))

