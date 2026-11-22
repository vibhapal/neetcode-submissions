class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        max_count =1
        sorted_nums = sorted(set(nums))

        for i in range(len(sorted_nums)-1):
            if sorted_nums[i+1] == sorted_nums[i]+1:
                count +=1
            else:
                max_count = max(max_count, count)
                count = 1
            
            max_count = max(max_count, count)
        return max_count