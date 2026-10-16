class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[position[i], speed[i]] for i in range(len(position))]  #[position, speed]
        pos_speed.sort(key=lambda x: x[0])
        time = []
        for p, s in pos_speed: 
            t = ((target - p) / s)
            while time and t >= time[len(time) - 1]: 
                time.pop()
            time.append(t)
        return len(time)

            
            