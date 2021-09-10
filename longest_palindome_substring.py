class Solution:
   
            
    def longestPalindrome(self, s: str) -> str:
        best_sub =''
        longest =  0 
        for cur in range(len(s)):
            #odd length case 
            left ,right  = cur,cur 
            while(left >=0 and right <len(s) and s[left] ==s[right]):
                if right-left +1 > longest : 
                    longest  =right-left+1 # len
                    best_sub  = s[left:right+1]
                left-=1
                right+=1
            # even length case 
            left ,right  = cur,cur+1 
            while(left >=0 and right <len(s) and s[left] ==s[right]):
                if right-left+1  > longest : 
                    longest  =right-left+1  # len
                    best_sub  = s[left:right+1]
                left-=1
                right+=1
        return best_sub
                
