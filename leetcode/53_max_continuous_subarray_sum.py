class Solution:
    def maxContiguousSubarraySum(self, nums):
        max_so_far = nums[0]
        max_ending_here = nums[0]


        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here+nums[i], nums[i])
            max_so_far = max(max_ending_here, max_so_far)

        return max_so_far