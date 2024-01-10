class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k=True
        s=list(s)
        t=list(t)
        m=set(s)
        n=set(t)
        if len (m)!=len(n):
            k=False
        if len(s)!=len(t):
            k=False
        for i in m:
            if i not in n:
                k=False
            else:
                a1=s.count(i)
                a2=t.count(i)
                if a1!=a2:
                    k=False
        for i in n:
            if i not in m:
                k=False
            else:
                a1=s.count(i)
                a2=t.count(i)
                if a1!=a2:
                    k=False

        return k