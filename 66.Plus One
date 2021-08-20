class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        carry  = 0
        
        while  i >= 0:
            if(i==len(digits)-1):
                digits[i]+=1
            digits[i]+= carry
            
            carry  = digits[i]//10
            digits[i]%=10
            i-=1
        if carry:
            digits.insert(0,1)
        return digits
