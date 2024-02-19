class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list = []
        list.append(nums[0])
        for i in range(1, len(nums)):
            list.append(list[i-1]+nums[i])
        return list