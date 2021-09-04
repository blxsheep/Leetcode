class Solution:
    def reverse(self, x: int) -> int:
        minus =  1
        while(x%10 ==0 and x!=0):
            x/=10
        x = int(x)
        if(x<0):
            x*=-1 
            minus = -1
            
        temp  = str(x)
        temp = temp[::-1]
        ans = int(temp)
        ans*=minus
        if ans >= pow(2,31) or ans < -1*pow(2,31) :
            ans  = 0 
        return ans
        
