class TripleInOne:
    def __init__(self, stackSize: int):
        self.stack_size = stackSize
        self.data = [[], [], []]

    def push(self, stackNum: int, value: int) -> None:
        if len(self.data[stackNum]) < self.stack_size:
            self.data[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if len(self.data[stackNum]):
            return self.data[stackNum].pop()
        return -1

    def peek(self, stackNum: int) -> int:
        if len(self.data[stackNum]):
            return self.data[stackNum][-1]
        return -1

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.data[stackNum]) == 0

