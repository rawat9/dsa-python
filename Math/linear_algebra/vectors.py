import numpy as np
from math import sqrt
from numpy.linalg import eig, det


class Vector:
    def determinant(self, m: list[list]):
        """
        Determinant of the given matrix m

        Parameters
        ----------
        m : matrix array

        Returns
        -------
        det: int

        Examples
        --------
        >>> np.linalg.det([[1,0], [0,1]])
        1.0
        >>> np.linalg.det([[1,1,1],[4,2,1],[6,7,0]])
        15.0
        """
        return det(np.array(m))

    def dot_product(self, u: list, v: list) -> int:
        return np.dot(u, v)

    def cross_product(self, u: list, v: list) -> int:
        return np.cross(u, v)

    def magnitude(self, u: list) -> float:
        return sqrt(sum(list(map(lambda x: x**2, np.array(u)))))

    def eigen(self, m: list[list]):
        eigenvalues, eigenvectors = eig(np.array(m))
        np.set_printoptions(precision=4)
        print('Eigenvalues:' , eigenvalues)
        print('Eigenvectors:', eigenvectors)


if __name__ == '__main__':  
    import doctest
    doctest.testmod()