# Generalized Matrix and Vector Interface

**A Python framework for working with multiple matrix representations through a unified interface.**

**Author:** Vaishnav Pula

---

## Overview

This project implements a generalized Matrix and Vector interface that allows multiple matrix representations to be used with the same numerical algorithms.

The implemented backends are:

- Dense Matrix
- CSR (Compressed Sparse Row) Matrix
- Banded Matrix
- Block Matrix

The project includes matrix-vector multiplication, transpose operations, Power Iteration, Jacobi Iterative Solver, correctness testing, and performance measurement.

---

## Key Features

- Common abstract `Matrix` interface
- `Vector` implementation
- Dense, CSR, Banded, and Block matrices
- Matrix-vector multiplication
- Matrix transpose
- Python `@` operator support
- Power Iteration
- Jacobi Iterative Solver
- Cross-backend correctness testing
- Performance benchmarking
- Large-scale sparse matrix testing

---

## Architecture

```text
                    Matrix Interface
                           │
          ┌────────────────┼────────────────┐
          │                │                │
        Dense              CSR            Banded
          │                │                │
          └────────────────┼────────────────┘
                           │
                         Block
                           │
                           ▼
              Numerical Algorithms
                           │
              ┌────────────┴────────────┐
              │                         │
       Power Iteration          Jacobi Solver
```

---

## Project Structure

```text
Generalized-Matrix-Vector-Interface/
│
├── source_code.py
├── larger_band_matrix.py
├── README.md
├── report.pdf
├── requirements.txt
├── AI-use-declaration.txt
│
└── Screenshots/
    ├── interface.png
    ├── testing-results.png
    ├── performance.png
    └── output.png
```

---

## Requirements

- Python 3.13 or compatible Python 3 version
- No external libraries required

---

## How to Run

### Main Program

```bash
python source_code.py
```

### Large-Scale Test

```bash
python larger_band_matrix.py
```

---

## Large-Scale Test

The project includes a separate test using a:

```text
100,000 × 100,000
```

sparse tridiagonal matrix.

The matrix contains:

- `100,000` main-diagonal values
- `99,999` upper-diagonal values
- `99,999` lower-diagonal values

**Total non-zero values:** `299,998`

The matrix is handled using a banded/tridiagonal approach instead of creating a full dense matrix.

The test verifies:

- Matrix shape
- Diagonal access
- Zero-region access
- Matrix-vector multiplication
- Result elements
- Execution time

---

## Documentation

For detailed implementation, algorithms, testing results, and performance information, see:

**`report.pdf`**

Test execution screenshots are available in the **`Screenshots/`** directory.

---

## Author

**Vaishnav Pula**
