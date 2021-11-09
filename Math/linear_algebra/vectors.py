import numpy as np
from math import acos, sqrt
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
        """
        Calculate the dot product of two vectors u, v
        """
        return np.dot(u, v)

    def cross_product(self, u: list, v: list) -> int:
        """
        Calculate the cross product of two vectors u, v
        """
        return np.cross(u, v)

    def magnitude(self, u: list) -> float:
        """
        Calculate the magnitude of vector u
        """
        return sqrt(sum(list(map(lambda x: x ** 2, np.array(u)))))

    def angle(self, u, v):
        """
        Angle between two vectors: u, v in radians
        """
        return acos(self.dot_product(u, v) / (self.magnitude(u) * self.magnitude(v)))

    def eigen(self, m: list[list]):
        """
        Calculate eigenvalues and eigenvectors of
        """
        eigenvalues, eigenvectors = eig(np.array(m))
        np.set_printoptions(precision=4)
        print("Eigenvalues:", eigenvalues)
        print("Eigenvectors:", eigenvectors)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
