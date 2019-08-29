class Solution:
    def reverse(self, x):
        print(int(str(x)[::-1]))
        return int(str(x)[::-1])
        # rev = 0
    #     while x > 0:
    #         rev = (10*rev) + x%10
    #         num //= 10
    #     return rev

Solution.reverse(110)