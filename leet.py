# 1) Remove Duplicates from Dataset
class Solution:
    def removeDuplicates(self, nums: list[int]) -> list[int]:
        uniq_list = []
        for n in nums:
            if n not in uniq_list:
                uniq_list.append(n)
        return uniq_list
      
"""
Test case 1
Input: [1, 2, 2, 3, 1, 4]
Output: [1, 2, 3, 4]

Test case 2
Input: [5, 5, 5]
Output: [5]
"""
lst = Solution()
nums = [5,5,5]
print(lst.removeDuplicates(nums))


