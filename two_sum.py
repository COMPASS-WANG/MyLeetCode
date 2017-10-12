# author: Sinan Wang
# Oct 12th 2017

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic.keys():
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i
        return('ERROR')
