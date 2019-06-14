class Solution(object):
	
	def numDecodings(self, s):
		### **********************
		### dfs in not good enough.
		### **********************

		"""
		:type s: str
		:rtype: int
		"""
		if len(s) == 0 : 
			return 0 

		if s == "0":
			return 0 

		key = {}
		count = 1
		for i in range(26):
			#key[chr(i+ord('A'))] = count
			key[str(count)] = chr(i+ord('A'))
			count += 1

		ans = []
		def dfs(s, b=''):
			if len(s) == 0 :
				ans.append(b)
				return None

			if s[0] in key.keys():
				dfs(s[1:], b + key[s[0]])

			if len(s) >= 2:
				if s[:2] in key.keys():
					if int(s[:2]) <= 26 :
						dfs(s[2:], b + key[s[:2]])
		dfs(s)
		return len(ans)


b = Solution()
a = "101"
a = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
print(b.numDecodings(a))
