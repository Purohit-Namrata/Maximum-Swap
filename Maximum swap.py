class Solution:
    def maximumSwap(self, num: int) -> int:
        num=list(str(num))
        swap_i=swap_j=-1
        max_digit='0'
        max_i=-1
        for i in reversed(range(len(num))):
            if num[i]>max_digit:
                max_digit=num[i]
                max_i=i
            if num[i]<max_digit:
                swap_i,swap_j=i,max_i
        num[swap_i],num[swap_j]=num[swap_j],num[swap_i]
        return int("".join(num))
s=Solution()
print(s.maximumSwap(2736))