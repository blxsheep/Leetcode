class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 , p2 =  0,0
        #p1 point at now value 
        #p2 scanning for what it should be 
        if len(nums)==0 : return 0
        while p2 < len(nums) :
            if(nums[p1] ==nums[p2]):
                p2+=1 #move pointer
            else:
                p1+=1
                nums[p1] = nums[p2]#rewrite when find difference value
        return p1+1
            
                
