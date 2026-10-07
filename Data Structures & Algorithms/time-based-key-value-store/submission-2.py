class TimeMap:

    def __init__(self):
        self.ks = {} # {key: [val, timestamp]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ks:
            self.ks[key] = []
        self.ks[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        
        ret = ""
        vals = self.ks.get(key,[])
        l,r = 0, len(vals) - 1

        while l <= r:
            m = (l + r) // 2
            if vals[m][1] <= timestamp:
                ret = vals[m][0]
                l = m + 1
            else:
                r = m - 1
        return ret
        