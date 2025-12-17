import pytest

from algorithm_org.heap.heap import Heap


class TestMinHeap:

    def test_heap_constructor(self) -> None:
        """Test constructor or Heap object."""
        nums = [5, 3, 8, 1, 2]
        heap = Heap(nums)

        assert heap.pop() == 1
        assert heap.pop() == 2
        assert heap.pop() == 3
        assert heap.pop() == 5
        assert heap.pop() == 8

    def test_push_and_pop(self) -> None:
        """Test push and pop contemporarily."""
        heap = Heap()
        heap.push(10)
        heap.push(5)
        heap.push(1)

        assert len(heap) == 3
        assert heap.peek() == 1

        assert heap.pop() == 1
        assert heap.pop() == 5
        assert heap.pop() == 10

    def test_pop_abnormally(self) -> None:
        """Test pop function when raising IndexError."""
        heap = Heap()
        with pytest.raises(IndexError):
            heap.pop()

    def test_pushpop(self) -> None:
        """Test pushpop function."""
        nums = [5, 3, 8, 1, 4]
        heap = Heap(nums)
        ret_val = heap.pushpop(2)

        assert ret_val == 1
        assert heap.peek() == 2

    def test_replace(self) -> None:
        """Test replace function."""
        nums = [5, 3, 8, 1, 4]
        heap = Heap(nums)
        ret_val = heap.replace(10)

        assert ret_val == 1
        assert heap.peek() == 3

    def test_replace_abnormally(self) -> None:
        """Test replace function when raising IndexError."""
        heap = Heap()
        with pytest.raises(IndexError):
            heap.replace(1)


class TestMaxHeap:

    def test_heap_constructor(self) -> None:
        """Test constructor or Heap object."""
        nums = [5, 3, 8, 1, 2]
        nums = [-i for i in nums]
        heap = Heap(nums)

        assert -heap.pop() == 8
        assert -heap.pop() == 5
        assert -heap.pop() == 3
        assert -heap.pop() == 2
        assert -heap.pop() == 1

    def test_push_and_pop(self) -> None:
        """Test push and pop contemporarily."""
        heap = Heap()
        heap.push(-10)
        heap.push(-5)
        heap.push(-1)

        assert len(heap) == 3
        assert -heap.peek() == 10

        assert -heap.pop() == 10
        assert -heap.pop() == 5
        assert -heap.pop() == 1

    def test_pushpop(self) -> None:
        """Test pushpop function."""
        nums = [5, 3, 8, 1, 4]
        nums = [-i for i in nums]
        heap = Heap(nums)
        ret_val = heap.pushpop(-2)

        assert -ret_val == 8
        assert -heap.peek() == 5

    def test_replace(self) -> None:
        """Test replace function."""
        nums = [5, 3, 8, 1, 4]
        nums = [-i for i in nums]
        heap = Heap(nums)
        ret_val = heap.replace(-10)

        assert -ret_val == 8
        assert -heap.peek() == 10
