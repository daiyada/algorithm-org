"""
Reimplementing parts of the heapq library.
"""

from typing import List, Optional


class Heap:

    @property
    def heap(self) -> List[int]:
        """Define getter of self._heap."""
        return self._heap

    def __init__(self, nums: Optional[List[int]] = None) -> None:
        """Define Constructor."""
        self._heap = nums if nums else []
        if self._heap:
            self._heapify()

    def __len__(self) -> int:
        """Return length of heap."""
        return len(self._heap)

    def _shift_up(self, i: int) -> None:
        """Shift up child node to parent index."""
        while i > 0:
            parent_idx = (i - 1) // 2
            if self._heap[i] < self._heap[parent_idx]:
                self._heap[i], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[i],
                )
                i = parent_idx
            else:
                break

    def _shift_down(self, i: int) -> None:
        """Shift down parent node to child index."""
        n = len(self._heap)
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            smallest = i

            if (
                left_child < n
                and self._heap[left_child] < self._heap[smallest]
            ):
                smallest = left_child
            if (
                right_child < n
                and self._heap[right_child] < self._heap[smallest]
            ):
                smallest = right_child

            if smallest != i:
                self._heap[smallest], self._heap[i] = (
                    self._heap[i],
                    self._heap[smallest],
                )
                i = smallest
            else:
                break

    def _heapify(self) -> None:
        """Transform array to heap structure."""
        n = len(self._heap)
        for i in reversed(range(n // 2)):
            self._shift_down(i)

    def push(self, val: int) -> None:
        """Push value to heap."""
        self._heap.append(val)
        self._shift_up(len(self._heap) - 1)

    def pop(self) -> int:
        """Pop value from heap."""
        if not self._heap:
            raise IndexError("heap is None or empty.")
        last_val = self._heap.pop()
        if self._heap:
            return_val = self._heap[0]
            self._heap[0] = last_val
            self._shift_down(0)
            return return_val
        return last_val

    def pushpop(self, val: int) -> int:
        """Push new value and pop minimum value."""
        if self._heap and self._heap[0] < val:
            val, self._heap[0] = self._heap[0], val
            self._shift_down(0)
        return val

    def replace(self, val: int) -> int:
        """Replace minimum value and push new value."""
        if not self._heap:
            raise IndexError("heap is None or empty.")
        return_val = self._heap[0]
        self._heap[0] = val
        self._shift_down(0)
        return return_val

    def peek(self) -> int:
        """Just return minimum value. in heap."""
        if not self._heap:
            raise IndexError("heap is None or empty.")
        return self._heap[0]
