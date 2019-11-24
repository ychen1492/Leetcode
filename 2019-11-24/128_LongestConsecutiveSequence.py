from typing import List


def longestConsecutive(nums: List[int]) -> int:
    count = 0
    num_dict = {}
    for index1, num1 in enumerate(nums):
        num_dict[num1] = index1

    for key in num_dict.keys():
        pre_num = key - 1
        post_num = key + 1
        if pre_num in num_dict:
            count += 1
        elif post_num in num_dict:
            count += 1
        elif len(nums) == 0 or len(set(nums)) == 1:
            count = 1
    return count


# l = [100, 4, 200, 1, 3, 29]
l = [2147483646, -2147483647, 0, 2, 2147483644, -2147483645, 2147483645]
longestConsecutive(l)
