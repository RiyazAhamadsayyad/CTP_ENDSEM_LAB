# Question 10 – Generic Queue and Stack

## Aim

To develop a reusable Python program using generic Queue and Stack implementations with type hints and dataclasses. The Queue processes food orders using FIFO, while the Stack stores cancelled orders using LIFO.

## Problem Statement

An online food-delivery application receives customer orders continuously. Orders must be processed in FIFO order, while recently cancelled orders need to be maintained for possible restoration using LIFO order.

## Concepts Used

- Queue
- Stack
- FIFO (First In, First Out)
- LIFO (Last In, First Out)
- Generic Programming
- Type Hints
- Python Dataclasses
- Lists

## Algorithm

1. Import dataclass, field, Generic, TypeVar, and List.
2. Create a generic Queue class.
3. Implement enqueue() to add food orders.
4. Implement dequeue() to process the first order.
5. Create a generic Stack class.
6. Implement push() to store cancelled orders.
7. Implement pop() to restore the latest cancelled order.
8. Add Pizza and Burger to the Queue.
9. Process the first order using dequeue().
10. Add Fries and Pasta to the Stack.
11. Restore Pasta using pop().
12. Display the current Queue and Stack.

## Program

```python
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
```

## Expected Output

```text
Queue: ['Pizza', 'Burger']
Processed: Pizza
Stack: ['Fries', 'Pasta']
Restored: Pasta
Current Queue: ['Burger']
Current Stack: ['Fries']
```

## Explanation

The Queue stores food orders and follows FIFO, so Pizza is processed before Burger.

The Stack stores cancelled orders and follows LIFO, so Pasta is restored before Fries because Pasta was cancelled most recently.

Generic[T] makes the Queue and Stack reusable with different data types.

## Time Complexity

| Operation | Complexity |
|---|---|
| enqueue() | O(1) |
| dequeue() | O(n) |
| push() | O(1) |
| pop() | O(1) |

## Space Complexity

The overall space complexity is O(n) because the Queue and Stack store n elements.

## Result

The generic Queue and Stack were successfully implemented using Python dataclasses and type hints. Food orders were processed using FIFO, and cancelled orders were restored using LIFO.


## Viva Questions and Answers

### 1. What is a Queue?

A Queue is a linear data structure that follows **FIFO (First In, First Out)**.  
The element inserted first is removed first.  
Example: food orders are processed in the order they are received.

### 2. What is a Stack?

A Stack is a linear data structure that follows **LIFO (Last In, First Out)**.  
The element inserted last is removed first.  
Example: the latest cancelled order is restored first.

### 3. What is the use of `enqueue()` and `dequeue()`?

`enqueue()` is used to **add an item** to the Queue.  
`dequeue()` is used to **remove the first item** from the Queue.  
These operations help process orders in FIFO order.

### 4. What is the use of `push()` and `pop()`?

`push()` is used to **add an item** to the Stack.  
`pop()` removes the **most recently added item** from the Stack.  
These operations help restore cancelled orders in LIFO order.

### 5. Why is `Generic[T]` used in this program?

`Generic[T]` makes the Queue and Stack **reusable with different data types**.  
They can store strings, integers, or objects.  
It improves code flexibility and reusability.
