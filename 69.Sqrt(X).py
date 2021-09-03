class Solution:
    def mySqrt(self, x: int) -> int:
        #using binary-like method 
        if(x==1 or x ==0  ) : return x
        start ,end  = 1,x
        ans = 0 
        while start <=end : 
            mid =  (start+end)//2
            if mid*mid == x : return mid
            if mid*mid < x : # this mean answer maybe on right side
                start = mid +1
                ans =  mid # collect current best answer (tuncrate)
            else :
                end  = mid-1
        return ans
