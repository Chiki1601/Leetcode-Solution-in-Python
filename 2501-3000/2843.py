class Solution(object):
    def countSymmetricIntegers(self, low, high):
        ans=0
        while low<=high:
            x=low
            s=""
            while x>0:
                tem=x%10
                s+=chr(tem+ord('0'))
                x=(x // 10)
            sum1=0
            sum2=0
            if(len(s)%2==0 and len(s)>0):
                for i in range(0,len(s)//2):
                    sum1+=ord(s[i])-ord('0')
                for i in range(len(s)//2,len(s)):
                    sum2+=ord(s[i])-ord('0')
                if(sum1==sum2):
                    ans=ans+1
            low=low+1    
            
        return ans
