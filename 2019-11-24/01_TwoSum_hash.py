"""
    Using the hash table to search the
    index
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for index1, num1 in enumerate(nums):
        num2 = target - num1
        if num2 in num_dict:
            return [num_dict[num2], index1]
        num_dict[num1] = index1


nums = [20, 7, 2, 15]
targt = 9
print(twoSum(nums=nums, target=targt))
