class SetOfStacks():
    def __init__(self, stackSize):
        self.stackSize = stackSize or 10
        self.stacks = []

    def push(self, data):
        if len(self.stacks) == 0:
            self.stacks.append([])

        for index, stack in enumerate(self.stacks):
            if len(stack) < self.stackSize:
                self.stacks[index].append(data)
                return
            elif index == len(self.stacks)-1:
                newStack = []
                newStack.append(data)
                self.stacks.append(newStack)
                return
            

    def pop(self):
        for stack in reversed(self.stacks):
            stack_len = len(stack)
            if stack_len > 0:
                stack.pop()
                
                if stack_len == 1:
                    self.stacks.pop()

                return

    def popAt(self, index):
        if index <= len(self.stacks)-1:
            self.stacks[index].pop()


setOfStacks = SetOfStacks(5)
setOfStacks.push(1)
setOfStacks.push(2)
setOfStacks.push(3)
setOfStacks.push(4)
setOfStacks.push(5)
setOfStacks.push(6)
setOfStacks.push(7)
setOfStacks.push(8)
setOfStacks.push(9)
setOfStacks.push(10)
setOfStacks.push(11)
setOfStacks.pop()
setOfStacks.pop()
setOfStacks.push(10)
setOfStacks.push(11)
setOfStacks.popAt(1)
setOfStacks.popAt(0)
setOfStacks.push(5)
setOfStacks.push(10)

print(setOfStacks.stacks)