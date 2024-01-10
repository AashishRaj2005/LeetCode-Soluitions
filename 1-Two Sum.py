class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=len(nums)
        k=k-1
        m=[]
        for i in range (0,k):
            for j in range(k,i,-1):
                    if (nums[i]+nums[j])==target:
                        m.append(i)
                        m.append(j)
        return(m)
