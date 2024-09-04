class Solution(object):
    def twoSum(self, nums, target):
        
        dic = {}

        for i, num in enumerate(nums):
            baki=target-num
            
            if baki in dic:
                return ([dic[baki],i])
                
            else:
                dic[num]=i
        
 