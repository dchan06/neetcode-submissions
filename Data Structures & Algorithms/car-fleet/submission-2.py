class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[position[i], speed[i]] for i in range(len(position))]  #[position, speed]
        pos_speed.sort(key=lambda x: x[0])
        time = []
        for p, s in pos_speed[::-1]: # back to front because the speed of the fleet comes from the cars in front
            time.append((target - p) / s)
            if len(time) >= 2 and time[-1] <= time[-2]: 
                time.pop()
        return len(time)

            
            