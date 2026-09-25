import math
import time
from abc import ABC, abstractmethod


# ABSTRACT INTERFACE

class Matrix(ABC):

    @abstractmethod
    def shape(self):
        pass

    @abstractmethod
    def get(self, i, j):
        pass

    @abstractmethod
    def matVec(self, x):
        pass

    @abstractmethod
    def transpose(self):
        pass

    @property
    def T(self):
        return self.transpose()

    def __matmul__(self, x):
        return self.matVec(x)


# VECTOR

class Vector:

    def __init__(self, data):
        self.data = list(data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def __repr__(self):
        return str(self.data)


# DENSE MATRIX

class DenseMatrix(Matrix):

    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def shape(self):
        return self.rows, self.cols

    def get(self, i, j):
        return self.data[i][j]

    def matVec(self, x):
        result = []

        for i in range(self.rows):
            total = 0

            for j in range(self.cols):
                total += self.data[i][j] * x[j]

            result.append(total)

        return result

    def transpose(self):
        result = []

        for j in range(self.cols):
            row = []

            for i in range(self.rows):
                row.append(self.data[i][j])

            result.append(row)

        return DenseMatrix(result)

# CSR MATRIX

class CSRMatrix(Matrix):

    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

        self.values = []
        self.cols_idx = []
        self.row_ptr = [0]

        count = 0

        for row in data:
            for j in range(len(row)):

                if row[j] != 0:
                    self.values.append(row[j])
                    self.cols_idx.append(j)
                    count += 1

            self.row_ptr.append(count)

    def shape(self):
        return self.rows, self.cols

    def get(self, i, j):

        start = self.row_ptr[i]
        end = self.row_ptr[i + 1]

        for k in range(start, end):

            if self.cols_idx[k] == j:
                return self.values[k]

        return 0

    def matVec(self, x):
        result = []

        for i in range(self.rows):

            total = 0

            start = self.row_ptr[i]
            end = self.row_ptr[i + 1]

            for k in range(start, end):
                total += self.values[k] * x[self.cols_idx[k]]

            result.append(total)

        return result

    def transpose(self):
        result = []

        for j in range(self.cols):
            row = []

            for i in range(self.rows):
                row.append(self.get(i, j))

            result.append(row)

        return CSRMatrix(result)


# BANDED MATRIX

class BandedMatrix(Matrix):

    def __init__(self, data, lower=1, upper=1):
        self.data = data
        self.n = len(data)
        self.lower = lower
        self.upper = upper

    def shape(self):
        return self.n, self.n

    def get(self, i, j):

        if i - j > self.lower:
            return 0

        if j - i > self.upper:
            return 0

        return self.data[i][j]

    def matVec(self, x):
      result = []
  
      for i in range(self.n):

        total = 0

        start = max(0, i - self.lower)
        end = min(self.n, i + self.upper + 1)

        for j in range(start, end):
            total += self.data[i][j] * x[j]

        result.append(total)

      return result
    def transpose(self):
        result = []

        for j in range(self.n):
            row = []

            for i in range(self.n):
                row.append(self.data[i][j])

            result.append(row)

        return BandedMatrix(
            result,
            self.upper,
            self.lower
        )


# BLOCK MATRIX

class BlockMatrix(Matrix):

    def __init__(self, data, block=2):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        self.block = block

    def shape(self):
        return self.rows, self.cols

    def get(self, i, j):
        return self.data[i][j]

    def matVec(self, x):
        result = [0] * self.rows
        b = self.block

        for i in range(0, self.rows, b):

            for j in range(0, self.cols, b):

                for p in range(i, min(i + b, self.rows)):

                    for q in range(j, min(j + b, self.cols)):
                        result[p] += self.data[p][q] * x[q]

        return result

    def transpose(self):
        result = []

        for j in range(self.cols):
            row = []

            for i in range(self.rows):
                row.append(self.data[i][j])

            result.append(row)

        return BlockMatrix(result, self.block)


# POWER ITERATION

def power_iteration(A, n=50):

    x = [1.0] * A.shape()[0]

    for _ in range(n):

        y = A @ x

        total = 0

        for value in y:
            total += value * value

        s = math.sqrt(total)

        x = []

        for value in y:
            x.append(value / s)

    return x


# JACOBI METHOD

def jacobi(A, b, n=100):

    x = [0.0] * len(b)

    for _ in range(n):

        new = [0.0] * len(b)

        for i in range(len(b)):

            total = 0

            for j in range(len(b)):

                if i != j:
                    total += A.get(i, j) * x[j]

            new[i] = (
                b[i] - total
            ) / A.get(i, i)

        x = new

    return x


# COMPARISON

def close(a, b, tol=1e-5):

    for i in range(len(a)):

        if abs(a[i] - b[i]) > tol:
            return False

    return True


# MAIN

def main():
    rows = int(input("Enter no.of rows :"))
    cols = int(input("Enter no.of columns :"))
    data = []
    print("Enter the matrix :")
    for i in range(rows):
        row = list(map(int,input().split()))
        data.append(row)
    x = Vector(list(map(int,input("Enter the vector x :").split())))
    b = Vector(list(map(int,input("Enter the vector b :").split())))

    matrices = {
        "Dense": DenseMatrix(data),
        "CSR": CSRMatrix(data),
        "Banded": BandedMatrix(data),
        "Block": BlockMatrix(data)
    }

    print("GENERALIZED MATRIX INTERFACE\n")

    # RESULTS

    for name in matrices:

        A = matrices[name]

        print(name)
        print("Shape :", A.shape())
        print("MatVec:", A @ x)
        print("Power :", power_iteration(A))
        print("Jacobi:", jacobi(A, b))
        print()

    # CORRECTNESS

    print("CORRECTNESS")
    print("=" * 40)

    dense = matrices["Dense"]

    for name in matrices:

        A = matrices[name]

        if A.shape() != dense.shape():
            print(name, "FAIL")
            continue

        if not close(A @ x, dense @ x):
            print(name, "FAIL")
            continue

        if not close(
            power_iteration(A),
            power_iteration(dense)
        ):
            print(name, "FAIL")
            continue

        if not close(
            jacobi(A, b),
            jacobi(dense, b)
        ):
            print(name, "FAIL")
            continue

        print(name, "PASS")

    # PERFORMANCE

    print("\nPERFORMANCE")
    print("=" * 40)

    for name in matrices:

        A = matrices[name]

        start = time.perf_counter()

        for _ in range(1000):
            A @ x

        end = time.perf_counter()

        print(
            name,
            ":",
            round(end - start, 6),
            "seconds"
        )


if __name__ == "__main__":
    main()
    
    
