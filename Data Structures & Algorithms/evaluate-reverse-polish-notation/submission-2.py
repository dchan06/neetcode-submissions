class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number = []
        for token in tokens:  
            if token.strip("-").isdigit(): 
                number.append(int(token))
                continue 
            second = number.pop() 
            first = number.pop()
            match token: 
                case "+": 
                    number.append(first + second) 
                case "-": 
                    number.append(first - second) 
                case "*": 
                    number.append(first * second) 
                case "/": 
                    number.append(int(first/second)) 
        return number.pop()

                 