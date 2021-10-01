from array import Array

class Array2D:
    """Creates a 2-D array of size numRows x numCols"""
    def __init__(self, numRows, numCols):
        # Create a 1-D array to store an array reference for each row
        self._theRows = Array(numRows)

        # Create a 1-D array for each row of the 2-D array
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        """Returns number of rows in the 2-D Array"""
        return len(self._theRows)

    def numCols(self):
        """Returns number of columns in the 2-D Array"""
        return len(self._theRows[0])
    
    def clear(self, value):
        """Clears the array by setting every element to the given value"""
        for row in self._theRows:
            row.clear(value)

    def __getitem__(self, ndxTuple):
        """Gets the contents of the element at position [i,j]"""
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
    
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), "Array subscript out of range"

        return self._theRows[row][col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) ==  2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), "Array subscript out of range"
        
        self._theRows[row][col] = value


if __name__ == '__main__':
    arr = Array2D(3, 3)
    arr.clear(4)
    arr.__setitem__([1,2], 10)
    print(arr.__getitem__([1,2]))





