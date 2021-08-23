class Stack:
        def __init__(self):
                self.stack = []
                self.top = -1
                
        def Push(self,s):
                self.stack.append(s)
                self.top += 1
                
        def Pop(self):
                if self.Empty():
                        raise Exception("Underflow")
                self.stack.pop()
                self.top -= 1

        # return the index of the top element 
        def Top(self):
                return len(self.stack) - 1

        def Empty(self):
                if self.top < 0:
                        return True
                return False
        
        def toString(self):
                return self.stack

class MaxStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
    
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.stack.append(x)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        result = self.stack[-1]
        self.stack.pop()
        return result

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack[len(self.stack) - 1]

    """
    @return: An integer
    """
    def peekMax(self):
        # write your code here
        return max(self.stack)

    """
    @return: An integer
    """
    def popMax(self):
        # write your code here
        l = []
        result = 0
        for i in range(len(self.stack)):
            if self.stack[i] == self.peekMax():
                l.append(i)
        result = self.stack[l[-1]]
        self.stack.pop(l[-1])
        return result


if __name__ == '__main__':
    S = Stack()
    print(S.toString())


    print(S.Empty())
    #S.Pop()
    
    S.Push(1)
    S.Push(2)
    S.Push(3)
    print(S.toString())

    S.Pop()
    print(S.toString())
    print(S.Empty())
