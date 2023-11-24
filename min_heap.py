# Name: William Clements
# OSU Email: clemenwi@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 11/29/2023
# Description: MinHeap implementation using dynamic array class from assignment 2


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None: #passes the prescribed tests
        """
        Add a new object to the MinHeap while maintaining heap property.

        Parameters:
        - node (object): The object to be added to the MinHeap.

        Returns:
        None
        """
        # Append the new node to the end of the dynamic array
        self._heap.append(node)

        # Perform heapify-up to maintain the min-heap property
        self._heapify_up()

    def _heapify_up(self) -> None: #helper method for add. After adding a new element to the heap at the end of the dynamic array,
        # ensures that the min-heap property is restored by moving the newly added element to its correct position in the heap.
        """
        Restore the min-heap property by moving the last element up to its correct position.

        This method is called after adding a new element to the heap.

        Returns:
        None
        """
        index = self._heap.length() - 1  # Index of the last element

        while index > 0:
            parent_index = (index - 1) // 2  # Calculate the parent index

            # If the current node is smaller than its parent, swap them
            if self._heap[index] < self._heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _swap(self, i: int, j: int) -> None: #helper method for add
        """
        Swap elements at indices i and j in the MinHeap's underlying dynamic array.

        Parameters:
        - i (int): Index of the first element to swap.
        - j (int): Index of the second element to swap.

        Returns:
        None
        """
        temp = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = temp

    def is_empty(self) -> bool: #passes the prescribed tests
        """
        Check if the heap is empty.

        Returns:
        bool: True if the heap is empty, False otherwise.
        """

        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Get the object with the minimum key in the heap without removing it.

        Returns:
        object: The object with the minimum key.

        Raises:
        MinHeapException: If the heap is empty.
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")

        return self._heap[0]

    def remove_min(self) -> object: #passes the prescribed test
        """
        Remove and return the object with the minimum key from the heap.

        Returns:
        object: The object with the minimum key.

        Raises:
        MinHeapException: If the heap is empty.
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")

        # Get the minimum element
        min_element = self._heap[0]

        # Replace the root element with the last element
        self._heap[0] = self._heap[self._heap.length() - 1]
        self._heap.remove_at_index(self._heap.length() - 1)

        # Perform heapify-down to maintain the min-heap property
        index = 0
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            # Compare with left child
            if left_child < self._heap.length() and self._heap[left_child] < self._heap[smallest]:
                smallest = left_child

            # Compare with right child
            if right_child < self._heap.length() and self._heap[right_child] < self._heap[smallest] and self._heap[
                right_child] != self._heap[left_child]:
                smallest = right_child

            # If the smallest is not the current node, swap and continue heapify-down
            if smallest != index:
                self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
                index = smallest
            else:
                break

        return min_element

    def build_heap(self, da: DynamicArray) -> None: #passes the prescribed test
        """
        Build a proper MinHeap from the given DynamicArray.

        Args:
        - da (DynamicArray): The DynamicArray with objects in any order.

        Returns:
        None
        """
        # Copy the elements from the provided DynamicArray to the MinHeap
        self._heap = DynamicArray(da)

        # Start from the last non-leaf node and perform heapify-down
        last_non_leaf = (self._heap.length() - 2) // 2
        for i in range(last_non_leaf, -1, -1):
            self._heapify_down(index=i)

    def _heapify_down(self, index: int) -> None:
        """
        Perform heapify-down operation starting from the given index.

        Args:
        - index (int): The index to start the heapify-down operation.

        Returns:
        None
        """
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            # Compare with left child
            if left_child < self._heap.length() and self._heap[left_child] < self._heap[smallest]:
                smallest = left_child

            # Compare with right child
            if right_child < self._heap.length() and self._heap[right_child] < self._heap[smallest]:
                smallest = right_child

            # If the smallest is not the current node, swap and continue heapify-down
            if smallest != index:
                self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
                index = smallest
            else:
                break

    def size(self) -> int:
        """
        Return the number of items currently stored in the heap.

        Returns:
        int: The number of items in the heap.
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clear the contents of the heap.

        Returns:
        None
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None: #passes the prescribed tests
    """
    Sorts the given DynamicArray in non-ascending order using Heapsort.

    Args:
        da (DynamicArray): The DynamicArray to be sorted.

    Returns:
        None
    """

    # Build a min-heap from the DynamicArray
    min_heap = MinHeap()
    for element in da:
        min_heap.add(element)

    # Sort the array in place using the min-heap
    for i in range(da.length() - 1, -1, -1):
        min_element = min_heap.remove_min()
        da[i] = min_element


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    """
    pass
