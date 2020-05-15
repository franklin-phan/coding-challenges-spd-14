class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count
removeElement(nums:['a','b','c'],val: 'b')
removeElement(nums:[1,2,3],val: 2)

nums = [1,2,3]
#nums = [3.3,5.6,99]
dif_num=1
if nums==[]:
    return 0

for i in range(len(nums)):
    if(i+1<len(nums)):
        if nums[i]<nums[i+1]:
            nums[dif_num]=nums[i+1]
            dif_num+=1
            
print(nums)
return dif_num
