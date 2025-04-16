class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        elements_in_current_window=dict()
        pair_count=0
        start=0
        end=0
        ans=0
        while(end<len(nums)):
            if(elements_in_current_window.has_key(nums[end])):
                elements_in_current_window[nums[end]]+=1 #incrementing 
            else:
                elements_in_current_window[nums[end]]=1 #initializing entry in the dictionary
            pair_count+=elements_in_current_window[nums[end]]-1 #counting number of pairs
            while pair_count>=k: #The shrinking phase
                ans+=1+len(nums)-end-1 #the number of new sequences
                elements_in_current_window[nums[start]]-=1 #remove the element at the starting of the window
                pair_count-=elements_in_current_window[nums[start]]
                start+=1
            end+=1    
        return ans            
            
        
