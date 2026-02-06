def divideArray(self, nums, k):
    nums.sort()
    tempList = []
    retList = []
    if nums[len(nums) - 1] - nums[len(nums) - 2] <= k:
        while len(nums) > 0:
            item1 = nums.pop(0)
            item2 = nums.pop(0)
            item3 = nums.pop(0)
            if item3 - item1 <= k:
                tempList.append(item1)
                tempList.append(item2)
                tempList.append(item3)
                retList.append(tempList)
                tempList = []
            else:
                retList = []
                break
    return retList