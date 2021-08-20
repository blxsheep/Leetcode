class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #keep difference in dict then search if in list has number in dict
        ans  = []
        dic =  dict()
        for i in range(len(nums)):
            dif =   target - nums[i]
            if nums[i] in dic :
                return [dic[nums[i]],i]
            else :
                dic[dif] = i
