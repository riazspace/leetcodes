class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        arr_size = len(nums)
        for i in range(arr_size):
            for j in range(i):
                if i == j:
                    continue
                elif nums[i]+ nums[j] == target:
                    output.append(i)
                    output.append(j)
        return output
