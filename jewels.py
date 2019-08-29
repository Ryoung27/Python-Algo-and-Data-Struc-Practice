class Solution:
    # J = "aA"
    # s="aAAbbbb"
    def numJewelsInStones(J, S):
        jewels = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    jewels = jewels + 1
        print(jewels)


    numJewelsInStones(J = "aA", S="aAAbbbb")