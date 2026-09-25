# Assignment 7 — Generalized Matrix and Vector Interface

## How to Run

1. Install Python 3.13 or a compatible Python 3 version.

2. No external libraries are required. The programs use only Python standard-library modules.

3. Open a terminal in the project folder.

4. Run the main program:

```text
python source_code.py
```

5. The large-matrix test can be executed separately using its test program.

---

## Environment Used for Verification

* **Python:** CPython 3.13.5
* **Platform:** Windows 64-bit operating system, x64-based processor
* **External Libraries:** None

### Standard-Library Modules Used

* `abc`
* `math`
* `time`

---

## Program Contents

The assignment implements:

* A common abstract `Matrix` interface
* `Vector`
* Dense Matrix
* CSR Matrix
* Banded Matrix
* Block Matrix
* Matrix-vector multiplication
* Matrix element access using `get(i, j)`
* Matrix transpose
* Power Iteration
* Jacobi Iterative Solver
* Cross-backend correctness testing
* Performance measurement

---

## Main Test Matrix

The main program uses the following **4 × 4 tridiagonal matrix**:

```text
[4 1 0 0]
[1 4 1 0]
[0 1 4 1]
[0 0 1 4]
```

The vector used for matrix-vector multiplication is:

```text
[1, 2, 3, 4]
```

The right-hand-side vector used for the Jacobi solver is:

```text
[5, 6, 6, 5]
```

The same logical matrix is represented using four different backends:

* Dense
* CSR
* Banded
* Block

The same backend-independent algorithms are applied to all four representations.

---

## Algorithms

### Power Iteration

Power Iteration repeatedly performs matrix-vector multiplication and normalization to approximate the dominant eigenvector.

### Jacobi Iterative Solver

The Jacobi method is used to iteratively solve:

```text
Ax = b
```

The same Jacobi algorithm is applied to all four matrix representations through the common `Matrix` interface.

---

## Correctness Testing

The results of the different matrix backends are compared with the Dense representation.

The following are checked:

* Matrix shape
* Matrix-vector multiplication
* Power Iteration result
* Jacobi solver result

A tolerance of `1e-5` is used when comparing numerical results because floating-point calculations can have small numerical differences.

The expected correctness result is:

```text
Dense PASS
CSR PASS
Banded PASS
Block PASS
```

---

## Performance Measurement

The program measures the execution time of repeated matrix-vector multiplication for each backend.

The timing is measured using Python's high-resolution performance timer.

Performance timings depend on the computer and execution environment.

---

## Large-Scale Test

A separate large-scale test was performed using a:

```text
100,000 × 100,000
```

sparse tridiagonal matrix.

The matrix contains three non-zero diagonals:

* Main diagonal: `100,000` values
* Upper diagonal: `99,999` values
* Lower diagonal: `99,999` values

Therefore, the total number of non-zero values is:

```text
100000 + 99999 + 99999 = 299998
```

The large matrix is represented using a banded/tridiagonal approach rather than creating a full `100000 × 100000` two-dimensional Python list.

The large-scale test verifies:

* Matrix shape
* Main diagonal access
* Upper diagonal access
* Lower diagonal access
* Zero-region access
* Matrix-vector multiplication
* First result element
* Middle result element
* Last result element
* Matrix-vector multiplication execution time

For the test vector containing all ones:

```text
x = [1, 1, 1, ..., 1]
```

the expected matrix-vector multiplication results are:

```text
First element  = 5
Middle element = 6
Last element   = 5
```

---

## Test Status

The submitted source code was executed successfully.

The main 4 × 4 test verifies the four matrix backends and the backend-independent algorithms.

The separate large-scale test verifies the handling of a 100,000 × 100,000 sparse tridiagonal matrix.

The test evidence contains the PASS/FAIL results and measured execution times from the verification runs.

---

## Implementation Notes

The abstract `Matrix` interface contains:

```text
shape()
get(i, j)
matVec(x)
transpose()
```

The `@` operator is implemented so that:

```python
A @ x
```

calls the matrix's `matVec()` method.

This allows the same algorithms to operate on Dense, CSR, Banded, and Block matrix representations without changing the algorithm code.

---

## Important

Performance timings are machine- and environment-dependent. The timings shown in the test evidence are the timings obtained during the verification runs used for this submission.

The 4 × 4 matrix is used for the main cross-backend correctness tests, while the 100,000 × 100,000 sparse tridiagonal matrix is used for the separate large-scale test.
