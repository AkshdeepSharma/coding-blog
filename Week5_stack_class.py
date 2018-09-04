class Stack:
    def __init__(self):
        self._element = []

    def empty(self):
        return len(self._element) == 0

    def push(self, value):
        self._element.append(value)

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        popped_element = self._element.pop()
        return popped_element

    def peek(self):
        if self.empty():
            raise IndexError('peek(): empty stack')
        return self._element[-1]

