**Author:** Vaishnav Pula
# Generalized Matrix and Vector Interface

A Python-based generalized matrix and vector framework that provides a common interface for multiple matrix representations, including Dense, CSR, Banded, and Block matrices.

The project demonstrates matrix abstraction, matrix-vector multiplication, transpose operations, iterative numerical algorithms, cross-backend correctness testing, and performance measurement.

---

## Overview

The project implements a common abstract `Matrix` interface that allows different matrix representations to be used with the same algorithms.

The following matrix representations are implemented:

- Dense Matrix
- CSR Matrix
- Banded Matrix
- Block Matrix

A common interface ensures that algorithms do not need to be rewritten for each matrix representation.

---

## Features

- Abstract `Matrix` interface
- `Vector` implementation
- Dense Matrix representation
- CSR Matrix representation
- Banded Matrix representation
- Block Matrix representation
- Matrix element access using `get(i, j)`
- Matrix-vector multiplication
- Matrix transpose
- Python `@` operator support for matrix-vector multiplication
- Power Iteration
- Jacobi Iterative Solver
- Cross-backend correctness testing
- Performance measurement
- Large-scale sparse matrix testing

---

## Project Structure

```text
Generalized-Matrix-Vector-Interface/
│
├── source_code.py
├── larger_band_matrix.py
├── README.md
├── report.pdf
├── AI-use-declaration.txt
│
└── screenshots/
    ├── ...
    └── ...
