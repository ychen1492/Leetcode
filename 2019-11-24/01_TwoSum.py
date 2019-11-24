from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        second_num = target - nums[i]
        if second_num in nums[i+1:]:
            return [i, nums.index(second_num)]


nums = [2,7,11,15]
targt = 9
print(twoSum(nums=nums, target=targt))