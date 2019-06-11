class Solution:
    def intersection(self, nums1, nums2):
        nums1= set(nums1)
        nums2 = set(nums2)
        print(nums1)
        print(nums2)
        ans =list(nums1 & nums2)
        return ans 

b = Solution()
a = [1,2,2,3,4]
c = [1,2,2]
print(b.intersection(a, c))