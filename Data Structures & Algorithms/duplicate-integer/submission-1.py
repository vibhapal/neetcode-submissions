class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        templist = []
        for i in range(len(nums)):
            if nums[i] in templist:
                return True
            templist.append(nums[i])
        return False

        