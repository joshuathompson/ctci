# Lots of this could be much simpler just using reversed() but it feels against the spirit not to reverse the elements one by one
class MyQueue():
    def __init__(self):
        self.queueStack = []
        self.dequeueStack = []

    def enqueue(self, item):
        self.queueStack.append(item)

    def dequeue(self):
        for item in self.queueStack:
            self.dequeueStack.insert(0, item)

        self.queueStack = []
        self.dequeueStack.pop()

        for item in self.dequeueStack:
            self.queueStack.insert(0, item)

        self.dequeueStack = []

    def peek(self):
        for item in self.queueStack:
            self.dequeueStack.insert(0, item)

        self.queueStack = []
        returnItem = None

        if len(self.dequeueStack) > 0:
            returnItem = self.dequeueStack[len(self.dequeueStack)-1]

        for item in self.dequeueStack:
            self.queueStack.insert(0, item)

        self.dequeueStack = []

        return returnItem

    def isEmpty(self):
        return len(self.queueStack) == 0

queue = MyQueue()

if queue.isEmpty():
    print("Queue is empty")

queue.enqueue("Billy")
queue.enqueue("Jane")
queue.enqueue("Test Guy")
queue.enqueue("Joshua")
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())

if not queue.isEmpty():
    print("Queue is not empty")