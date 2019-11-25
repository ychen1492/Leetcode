from typing import List


def longestConsecutive(nums: List[int]) -> int:
    """
           Build a hash to find whether a num in nums or not in O(1) time.
           """
    nums_dict = {num: False for num in nums}
    max_length = 0
    for num in nums:
        if nums_dict[num]:
            continue

        # Find the post consecutive number
        next_num = num + 1
        while next_num in nums_dict:
            nums_dict[next_num] = True
            next_num += 1

        # Find the pre consecutive number
        pre_num = num - 1
        while pre_num in nums_dict:
            nums_dict[pre_num] = True
            pre_num -= 1

        max_length = max(next_num - pre_num - 1, max_length)

    return max_length


# l = [100, 4, 200, 1, 3, 29]
# l = [2147483646, -2147483647, 0, 2, 2147483644, -2147483645, 2147483645]
# l = [1,2]
l=[9,1,4,7,3,-1,0,5,8,-1,6]
longestConsecutive(l)

