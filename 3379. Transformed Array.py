class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        MAX_SIZE = len(nums)

        for i in range(MAX_SIZE):
            if nums[i] != 0:
                result.append(nums[(i + nums[i]) % MAX_SIZE])
            else:
                result.append(nums[i])

        return result


soln = Solution()
nums = [-1, 4, -1]
print(soln.constructTransformedArray(nums))
