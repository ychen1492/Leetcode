class Solution:
    def findComplement(self, num:int)->int:
        tmp = num
        bit = 1
        while tmp:
            num = num^bit
            bit = bit<<1
            tmp = tmp>>1
        return num

if __name__ == "__main__":
    num_complement = Solution().findComplement(1)