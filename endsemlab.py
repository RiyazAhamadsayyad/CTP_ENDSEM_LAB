from dataclasses import dataclass, field
from typing import Generic, TypeVar, List

T = TypeVar("T")

@dataclass
class Queue(Generic[T]):
    items: List[T] = field(default_factory=list)

    def enqueue(self, x: T):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)

@dataclass
class Stack(Generic[T]):
    items: List[T] = field(default_factory=list)

    def push(self, x: T):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

q = Queue[str]()
s = Stack[str]()

q.enqueue("Pizza")
q.enqueue("Burger")

print("Queue:", q.items)
print("Processed:", q.dequeue())

s.push("Fries")
s.push("Pasta")

print("Stack:", s.items)
print("Restored:", s.pop())

print("Current Queue:", q.items)
print("Current Stack:", s.items)
