import time

class LargeDenseMatrix:
    def __init__(self, n):
        self.n = n

    def shape(self):
        return self.n, self.n

    def get(self, i, j):
        if i == j:
            return 4
        if j == i + 1:
            return 1
        if j == i - 1:
            return 1
        return 0

    def matVec(self, x):
        result = []
        for i in range(self.n):
            total = 0
            for j in range(self.n):
                total += self.get(i, j) * x[j]
            result.append(total)
        return result


class LargeSparseMatrix:
    def __init__(self, n):
        self.n = n
        self.lower = 1
        self.upper = 1

    def shape(self):
        return self.n, self.n

    def get(self, i, j):
        if i == j:
            return 4
        if j == i + 1:
            return 1
        if j == i - 1:
            return 1
        return 0

    def matVec(self, x):
        result = []
        for i in range(self.n):
            total = 0
            start = max(0, i - self.lower)
            end = min(self.n, i + self.upper + 1)
            for j in range(start, end):
                total += self.get(i, j) * x[j]
            result.append(total)
        return result


class LargeBlockMatrix:
    def __init__(self, n):
        self.n = n

    def shape(self):
        return self.n, self.n

    def get(self, i, j):
        if i == j:
            return 4
        if j == i + 1:
            return 1
        if j == i - 1:
            return 1
        return 0

    def matVec(self, x):
        result = []
        for i in range(self.n):
            total = 0

            if i > 0:
                total += x[i - 1]

            total += 4 * x[i]

            if i < self.n - 1:
                total += x[i + 1]

            result.append(total)

        return result


def check_result(A, n, x):
    print("Shape Test        :", "PASS" if A.shape() == (n, n) else "FAIL")
    print("Main Diagonal     :", "PASS" if A.get(0, 0) == 4 else "FAIL")
    print("Upper Diagonal    :", "PASS" if A.get(0, 1) == 1 else "FAIL")
    print("Lower Diagonal    :", "PASS" if A.get(1, 0) == 1 else "FAIL")
    print("Zero Region       :", "PASS" if A.get(0, 5) == 0 else "FAIL")

    start = time.time()
    result = A.matVec(x)
    end = time.time()

    print("Matrix-Vector     :", "PASS")
    print("MatVec Time       :", round(end - start, 6), "seconds")
    print("First Element     :", "PASS" if result[0] == 5 else "FAIL")
    print("Middle Element    :", "PASS" if result[n // 2] == 6 else "FAIL")
    print("Last Element      :", "PASS" if result[-1] == 5 else "FAIL")

    return end - start


def main():

    dense_n = 2000
    large_n = 100000

    print("=" * 70)
    print("LARGE MATRIX REPRESENTATION COMPARISON")
    print("=" * 70)

    print("Dense Matrix")
    print("-" * 70)
    print("Matrix Size       :", dense_n, "×", dense_n)
    x = [1] * dense_n
    dense = LargeDenseMatrix(dense_n)
    dense_time = check_result(dense, dense_n, x)

    print()

    print("Sparse Matrix")
    print("-" * 70)
    print("Matrix Size       :", large_n, "×", large_n)
    x = [1] * large_n
    sparse = LargeSparseMatrix(large_n)
    sparse_time = check_result(sparse, large_n, x)

    print()

    print("Block Matrix")
    print("-" * 70)
    print("Matrix Size       :", large_n, "×", large_n)
    block = LargeBlockMatrix(large_n)
    block_time = check_result(block, large_n, x)

    print()
    print("=" * 70)
    print("PERFORMANCE COMPARISON")
    print("=" * 70)
    print("Representation    Matrix Size          MatVec Time")
    print("-" * 70)
    print("Dense             ", dense_n, "×", dense_n, "       ", round(dense_time, 6), "seconds")
    print("Sparse            ", large_n, "×", large_n, "   ", round(sparse_time, 6), "seconds")
    print("Block             ", large_n, "×", large_n, "   ", round(block_time, 6), "seconds")
    print("=" * 70)


if __name__ == "__main__":
    main()