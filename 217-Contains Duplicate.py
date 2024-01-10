class Solution:
    def containsDuplicate(self, L1: List[int]) -> bool:
        x=False  
        L2=set(L1)
        if len(L2)<len(L1):
                x=True
        return (x)
        