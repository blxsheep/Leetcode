class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window method 
        best,start,end =  0,0,0
        dic =  dict()
        while end < len(s):
            if(s[end] in dic and dic[s[end]]>=start):
                start = dic[s[end]] +1            #sliding window when found 
                                                  #repeating in window
            
            cnt = end -start +1             
            if cnt > best : best  = cnt
            dic[s[end]]  =  end #update last index that visited
            end+=1
        return best
            
