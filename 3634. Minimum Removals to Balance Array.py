class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        # new_nums = sorted(nums)
        # curr, end_curr, curr_counter, new_counter = 0, 0, 0, 0
        # while len(new_nums)-curr  > new_counter:
        #     curr_counter = 0
        #     end_curr = curr
        #     while end_curr < len(new_nums) and new_nums[end_curr] <= k*new_nums[curr]:
        #         curr_counter += 1
        #         end_curr += 1
        #     curr += 1
        #     new_counter = max(new_counter,curr_counter)
        #
        # return len(nums)-new_counter


        # i = 0
        # while i < len(nums) and new_nums[i] <= k*new_nums[0]:
        #     i += 1
        # tot_deduc = len(nums)-i if i > 0 else 0
        # return tot_deduc
        nums.sort()
        left = 0
        max_window = 0

        for right in range(len(nums)):
            while nums[right] > k * nums[left]:
                left += 1
            max_window = max(max_window, right - left + 1)

        return len(nums) - max_window


soln = Solution()
nums = [1,34,26]
print(soln.minRemoval(nums, 4))

