def lengthOfLongestSubstring(s: str) -> int:
    start_index = 0
    end_index = 0
    max_length = 0
    char_dic = {}
    for i in range(len(s)):
        char = s[i]
        # character is already in the dictionary, start index increase 1
        if char in char_dic and start_index <= char_dic[char] <= end_index:
            start_index = char_dic[char] + 1
            end_index = i
        # character is not in the dictionary
        else:
            end_index = i
            if end_index - start_index + 1 > max_length:
                max_length = end_index-start_index+1
        char_dic[char] = i
    return max_length


s = 'pwwkewr'
lengthOfLongestSubstring(s)