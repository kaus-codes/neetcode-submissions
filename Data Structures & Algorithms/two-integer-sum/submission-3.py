class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #List, Tupple, Set, Dictionary
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]],i]
            dic[target - nums[i]] = i
        return []
