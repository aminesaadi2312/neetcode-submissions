class TimeMap:

    def __init__(self):
        self.dictionnaire = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionnaire[key].append((value, timestamp))

        
    def get(self, key: str, timestamp: int) -> str:
        best = ""
        pairs = self.dictionnaire[key]
        l, r = 0, len(pairs)-1
        while l <= r : 
            m = (l+r) // 2
            if pairs[m][1] <= timestamp : 
                best = pairs[m][0]
                l = m+1
            else :
                r = m-1
        return best
