import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, 'Array size must be > 0'
        self._size = size

        # Create the array structure using ctypes module
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

        # Initialize each element
        self.clear(None)

    def __len__(self):
        return self._size
        
    def __getitem__(self, index):
        if index > len(self):
            raise IndexError

        return self._elements[index]

    def __setitem__(self, index, value):
        if index > len(self):
            raise IndexError

        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, array):
        self.array = array
        self.curr_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_idx < len(self.array):
            element = self.array[self.curr_idx]
            self.curr_idx += 1
            return element
        else:
            raise StopIteration
