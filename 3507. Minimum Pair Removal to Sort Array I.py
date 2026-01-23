from operator import index


class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        while nums != sorted(nums):
            # minPos = nums.index(min(nums))
            # if minPos != len(nums) - 1 | minPos != 0:
            #     left = nums[minPos - 1]
            #     right = nums[minPos + 1]
            #     smallAdj = minPos - 1 if left < right else minPos + 1
            # elif minPos == 0:
            #     smallAdj = minPos + 1
            # elif minPos == len(nums) - 1:
            #     smallAdj = minPos - 1
            # nums[smallAdj] = nums[minPos] + nums[smallAdj]
            # nums.pop(minPos)
            minSum = float('inf')
            minIndex = -1
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < minSum:
                    minSum = current_sum
                    minIndex = i
            nums[minIndex] = minSum
            nums.pop(minIndex + 1)
            res += 1

        return res

result = Solution()
print(result.minimumPairRemoval([3,6,4,-6,2,-4,5,-7,-3,6,3,-4]))
