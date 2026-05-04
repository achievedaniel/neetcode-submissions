class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carSpeed = []
        for i in range(len(position)):
            carSpeed.append([position[i], speed[i]])
        carSpeed.sort(key=lambda args: args[0], reverse=True)

        stack = [(target - carSpeed[0][0]) / carSpeed[0][1]]

        for car in carSpeed:
            timeAtdestination = (target - car[0]) / car[1]
            if stack and timeAtdestination > stack[-1]:
                stack.append(timeAtdestination)

        return len(stack)
        