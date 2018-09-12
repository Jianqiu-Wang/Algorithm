class Solution:     
    def findMedianSortedArrays(self, nums1, nums2):
        """         
        :type nums1: List[int]         
        :type nums2: List[int]         
        :rtype: float         
        """         
        m = len(nums1)         
        n = len(nums2)         
        nums = []         
        i = 0         
        j = 0         
        while len(nums) <= m + n:             
            print(i,j, nums)             
            if nums1[i] <= nums2[j]:                 
                nums.append(nums1[i])                 
                if i < m - 1:                     
                    i = i + 1             
                else:                 
                    nums.append(nums2[j])                 
                    if j < n -1:                     
                        j = j + 1                 
                    else:                     
                        nums.append(nums1[i])

            print("lol")
            return nums[int((m+n)/2)]         
        else:
            print((m+n)/2-1, int((m+n)/2))
            print( nums[(m + n) / 2 - 1], nums[(m+n)/2])
            return (nums[(m+n)/2-1] + nums[(m+n)/2]) /2.


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    s = Solution()
    result = s.findMedianSortedArrays(nums1, nums2)
    print(result)
