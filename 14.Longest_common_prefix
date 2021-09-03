class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        last = 0 
        checker = strs[0]
        while last < len(checker) :
            for ele in strs :
                if(len(ele)-1 < last or ele[last]!= checker[last]):
                    return ele[0:last]
            last+=1
        return checker
                
