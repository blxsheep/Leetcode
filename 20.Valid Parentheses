class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        open  = ['(','{','[']
        close  = [')','}',']']
        for x in s :
            if len(stack)==0 and x in close : return False
            if x in open :
                stack.append(x)
                print('push open')
            if x in close :
                top = stack[-1]
                if top in close :
                    stack.append(x)
                    print('push close')
                elif open.index(top) == close.index(x):
                    stack.pop()
                    print('pop')
                else : 
                    stack.append(x)
                        
        return len(stack)==0
