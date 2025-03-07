class Queue:
    def __init__(self) -> None:
        self.items: list = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item: any) -> None:
        self.items.append(item)

    def dequeue(self) -> any:
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> any:
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Cannot peek from an empty queue")
