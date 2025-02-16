class Solution(object):
    def threeSum(self, nums):
        
        nums.sort()
        arr = []
        #print(nums)
        for i in range(len(nums)):
            x = nums[i]
            y = i + 1
            z = len(nums) - 1

            while y < z:
                if x + nums[y] + nums[z] == 0:
                    trip = [x, nums[y], nums[z]]
                    arr.append(trip)
                    y += 1
                    z -= 1  
                elif x + nums[y] + nums[z] > 0:
                    z -= 1
                else:
                    y += 1

        #print(arr)
        unique_arr = list(map(list, set(map(tuple, arr))))

        return(unique_arr)