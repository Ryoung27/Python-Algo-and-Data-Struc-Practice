class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        first_list = []
        second_list = []
        result = []
        for i in A:
            if i % 2 == 0:
                first_list.append(i)
            else:
                second_list.append(i)
        result = [None]*(len(first_list)+len(second_list))
        result[::2] = first_list
        result[1::2] = second_list
        return(result)