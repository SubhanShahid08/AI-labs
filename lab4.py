#Question1
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

obj1 = Stack()

while True:
    user_input = int(input("Enter a number to push onto the stack (-1 to terminate): "))
    if user_input == -1:
        break
    obj1.push(user_input)

obj1.display()

print("Popping")
popped_element = obj1.pop()
print(f"Popped element: {popped_element}")
obj1.display()

print("Peeking")
top_element = obj1.peek()
print(f"Top element: {top_element}")

#Question2
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)

obj1 = Queue()

while True:
    user_input = int(input("Enter a number to enqueue onto the queue (-1 to terminate): "))
    if user_input == -1:
        break
    obj1.enqueue(user_input)


obj1.display()


print("Dequeueing")
dequeued_element = obj1.dequeue()
print(f"Dequeued element: {dequeued_element}")
obj1.display()

print("Peeking")
front_element = obj1.front()
print(f"Front element: {front_element}")

#Question3
list1=[6,19,17,23,38,45,77,84,90]
num=int(input("Enter a number to find: "))
loc=False
list1.sort()
print(list1)
low = 0
high = len(list1) - 1
while low <= high:
    mid = (low + high) // 2
    if list1[mid] == num:
        loc=True
        break
    elif list1[mid] < num:
        low=mid+1
    elif list1[mid]> num:
        high=mid-1
if loc==True:
    print(f"{num} is found at index {mid}")   
else:
    print(f"{num} is not found in list")


