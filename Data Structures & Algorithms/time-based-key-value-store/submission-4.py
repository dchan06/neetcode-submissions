class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        key_list = self.time_map[key]
        l, r = 0, len(key_list) - 1
        m_timestamp, m_val = 0, ""
        timestamp_best = ""
        while l <= r: 
            m = l + ((r - l) // 2)
            m_timestamp, m_val = key_list[m]
            if m_timestamp == timestamp: 
                return m_val
            elif m_timestamp < timestamp: 
                timestamp_best = m_val
                l = m + 1
            else: 
                r = m - 1
        return timestamp_best

