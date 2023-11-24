from static_array import StaticArray

class DynamicArrayException(Exception):
    """Custom exception class to be used by Dynamic Array
DO NOT CHANGE THIS CLASS IN ANY WAY"""
    pass

class DynamicArray:
    def __init__(self, start_array=None):
        """Initialize new dynamic array DO NOT CHANGE THIS METHOD IN ANY WAY"""
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)
        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)
    def __str__(self) -> str:
        """Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY"""
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'
    def __iter__(self):
        """Create iterator for loop
    DO NOT CHANGE THIS METHOD IN ANY WAY"""
        self._index = 0
        return self
    def __next__(self):
        """Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY"""
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration
        self._index += 1
        return value
    def get_at_index(self, index: int) -> object:
        """Return value from given index position. Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY"""
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]
    def set_at_index(self, index: int, value: object) -> None:
        """Store value at given index in the array
Invalid index raises DynamicArrayException
DO NOT CHANGE THIS METHOD IN ANY WAY"""
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value
    def __getitem__(self, index) -> object:
        """Same functionality as get_at_index() method above,
    but called using array[index] syntax
    DO NOT CHANGE THIS METHOD IN ANY WAY"""
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY"""

        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY"""

        return self._size == 0

    def length(self) -> int:
        """Return number of elements stored in array
    DO NOT CHANGE THIS METHOD IN ANY WAY"""

        return self._size

    def get_capacity(self) -> int:
        """Return the capacity of the array
            DO NOT CHANGE THIS METHOD IN ANY WAY"""

        return self._capacity

    def print_da_variables(self) -> None:
        """Print information contained in the dynamic array.
        Used for testing purposes. DO NOT CHANGE THIS METHOD IN ANY WAY"""

        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")


# -----------------------------------------------------------------------
    def resize(self, new_capacity: int) -> None:  #passes the prescribed tests
        """Takes a positive integer as a parameter and changes the
        dynamic array's capacity to that number"""

        if new_capacity <= 0 or new_capacity < self._size:
            return  # Do nothing and exit if new_capacity is not valid

        new_data = StaticArray(new_capacity)
        for index in range(self._size):
            new_data.set(index, self._data.get(index))

        self._data = new_data
        self._capacity = new_capacity

    def append(self, value: object) -> None: #passes the prescribed tests
        """
            Appends the provided value to the dynamic array.

            Parameters:
            - value (object): The value to append to the dynamic array.

            If the internal storage is full (the size equals the capacity), this method
            doubles the capacity of the dynamic array to accommodate the new element.

            Returns:
            None
            """
        if self._size == self._capacity:
            # If the internal storage is full, double its capacity
            new_capacity = self._capacity * 2 if self._capacity > 0 else 1
            self.resize(new_capacity)

        self._data.set(self._size, value)
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None: #passes the prescribed tests
        """
            Inserts the given value at the specified index in the dynamic array.

            Parameters:
            - index (int): The index where the value should be inserted.
            - value (object): The value to insert in the dynamic array.

            If the internal storage is full (the size equals the capacity), this method
            doubles the capacity of the dynamic array to accommodate the new element.
            The elements at and after the specified index are shifted to make space for
            the new value.

            Raises:
            - DynamicArrayException: If the provided index is invalid (negative or
              greater than the current size).

            Returns:
            None
            """
        if index < 0 or index > self._size:
            raise DynamicArrayException("Invalid index")

        if self._size == self._capacity:
            # If the internal storage is full, double its capacity
            new_capacity = self._capacity * 2 if self._capacity > 0 else 1
            self.resize(new_capacity)

        # Shift elements to the right to make space for the new value
        for i in range(self._size, index, -1):
            self._data.set(i, self._data.get(i - 1))

        # Insert the new value at the specified index
        self._data.set(index, value)
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
            Removes the element at the specified index in the dynamic array.

            Parameters:
            - index (int): The index of the element to remove.

            If the size of the dynamic array is strictly less than 1/4 of its current
            capacity and the current capacity is greater than 10, this method reduces
            the capacity to twice the number of current elements, ensuring that the
            final capacity is at least 10.

            The elements after the specified index are shifted to fill the removed element's
            position, and the size is decremented.

            Raises:
            - DynamicArrayException: If the provided index is invalid (negative or
              greater than or equal to the current size).

            Returns:
            None
            """
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Invalid index")

        if self._capacity > 10 and self._size < self._capacity // 4:
            new_capacity = self._size * 2  # Double the size
            if new_capacity < 10:  # Ensure the new capacity is at least 10
                new_capacity = 10
            self.resize(new_capacity)

        # Shift elements to the left to fill the removed element's position
        for i in range(index, self._size - 1):
            self._data.set(i, self._data.get(i + 1))

        # Decrement the size
        self._size -= 1

    def slice(self, start_index: int, size: int) -> 'DynamicArray': #passes the prescribed tests.
        """
            Create a new dynamic array containing a slice of elements from the original array.

            Slices the dynamic array from the 'start_index' to 'start_index + size' (excluding the end index).

            Args:
            - start_index (int): The starting index for the slice.
            - size (int): The number of elements to include in the slice.

            Returns:
            - DynamicArray: A new dynamic array containing the sliced elements.

            Raises:
            - DynamicArrayException: If 'start_index' is out of range or 'size' is negative or the slice extends beyond the dynamic array's size.
            """
        if start_index < 0 or start_index >= self._size or size < 0:
            raise DynamicArrayException("Invalid start index or size")

        if start_index + size > self._size:
            raise DynamicArrayException("Not enough elements to create the slice")

        # Create a new DynamicArray for the slice
        slice_array = DynamicArray()

        # Append the requested elements to the slice_array
        for i in range(start_index, start_index + size):
            slice_array.append(self._data.get(i))

        return slice_array

    def merge(self, second_da: 'DynamicArray') -> None: #passes the prescribed tests
        """
            Merge the elements of another DynamicArray into the current DynamicArray.

            Appends each element from the provided 'second_da' DynamicArray to the end of the current DynamicArray.

            Args:
            - second_da (DynamicArray): The DynamicArray whose elements will be merged into the current DynamicArray.

            Returns:
            - None"""
        # Loop through the elements in the second DynamicArray
        for i in range(second_da.length()):
            # Append each element to the current DynamicArray
            self.append(second_da.get_at_index(i))

    def map(self, map_func) -> 'DynamicArray': #passes both prescribed tests
        """
            Create a new DynamicArray by applying a mapping function to each element.

            Applies the provided 'map_func' to each element of the current DynamicArray and stores the results
            in a new DynamicArray, which is then returned.

            Args:
            - map_func (function): The mapping function to be applied to each element in the current DynamicArray.
                This function should take one argument, which is an element from the current DynamicArray, and return
                the transformed value.

            Returns:
            - DynamicArray: A new DynamicArray containing the mapped values."""
        # Create a new DynamicArray to store the mapped values
        mapped_array = DynamicArray()
        for i in range(self.length()):
            # Apply the map_func to each element and append the result to the new array
            mapped_array.append(map_func(self.get_at_index(i)))
        return mapped_array

    def filter(self, filter_func): #passes the prescribed tests
        """
            Create a new DynamicArray by filtering elements based on a given predicate function.

            Filters the elements of the current DynamicArray based on the provided 'filter_func' and stores
            the elements that satisfy the filter criteria in a new DynamicArray, which is then returned.

            Args:
            - filter_func (function): The filtering function used to determine whether an element should be included
                in the filtered DynamicArray. This function should take one argument (an element from the current DynamicArray)
                and return a Boolean value (True if the element should be included, False if it should be excluded).

            Returns:
            - DynamicArray: A new DynamicArray containing the elements that satisfy the filter criteria."""
        # Create a new DynamicArray to store the filtered values
        filtered_array = DynamicArray()
        for i in range(self.length()):
            element = self.get_at_index(i)
            # Apply the filter_func to each element
            if filter_func(element):
                # If filter_func returns True, append the element to the new array
                filtered_array.append(element)
        return filtered_array

    def reduce(self, reduce_func, initializer=None): #passes the prescribed tests
        """
            Create a new DynamicArray by filtering elements based on a given predicate function.

            Filters the elements of the current DynamicArray based on the provided 'filter_func' and stores
            the elements that satisfy the filter criteria in a new DynamicArray, which is then returned.

            Args:
            - filter_func (function): The filtering function used to determine whether an element should be included
                in the filtered DynamicArray. This function should take one argument (an element from the current DynamicArray)
                and return a Boolean value (True if the element should be included, False if it should be excluded).

            Returns:
            - DynamicArray: A new DynamicArray containing the elements that satisfy the filter criteria."""
        if self.is_empty():
            return initializer

        if initializer is None:
            accumulator = self.get_at_index(0)
            start_index = 1
        else:
            accumulator = initializer
            start_index = 0

        for i in range(start_index, self.length()):
            element = self.get_at_index(i)
            accumulator = reduce_func(accumulator, element)

        return accumulator

def find_mode(arr: DynamicArray) -> (DynamicArray, int): #passes the prescribed test
    """
        Find the mode(s) and frequency of occurrence in a DynamicArray.

        Calculates the mode(s) and their frequency of occurrence in the provided 'arr' DynamicArray.
        The mode is the element(s) that appear most frequently in the array. If there are multiple modes,
        all of them are returned. The frequency represents how many times the mode(s) appear in the array.

        Args:
        - arr (DynamicArray): The DynamicArray to find the mode(s) in.

        Returns:
        - A tuple containing two elements:
          1. A DynamicArray of mode(s), where each mode appears most frequently in the input array.
          2. An integer representing the frequency of occurrence of the mode(s) in the input array."""
    if arr.is_empty():
        return DynamicArray(), 0

    max_frequency = 1
    current_frequency = 1
    mode_elements = DynamicArray()
    mode_elements.append(arr[0])

    for i in range(1, arr.length()):
        if arr[i] == arr[i - 1]:
            current_frequency += 1
        else:
            current_frequency = 1

        if current_frequency > max_frequency:
            mode_elements = DynamicArray()
            mode_elements.append(arr[i])
            max_frequency = current_frequency
        elif current_frequency == max_frequency:
            mode_elements.append(arr[i])

    return mode_elements, max_frequency