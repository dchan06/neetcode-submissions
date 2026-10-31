class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        key_list = self.time_map[key]
        l, r = 0, len(key_list) - 1
        m, m_timestamp, m_val = 0, 0, ""
        while l <= r: 
            m = l + ((r - l) // 2)
            m_timestamp, m_val = key_list[m]
            if m_timestamp == timestamp: 
                return m_val
            elif m_timestamp < timestamp: 
                l = m + 1
            else: 
                r = m - 1
        if m_timestamp < timestamp: 
            return m_val
        elif m > 0 and key_list[m - 1][0] < timestamp: 
            return key_list[m - 1][1]
        return ""

