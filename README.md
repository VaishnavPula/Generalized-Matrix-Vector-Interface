# Generalized Matrix and Vector Interface

**A Python framework for working with multiple matrix representations through a unified interface.**

**Author:** Vaishnav Pula

---

## Overview

This project implements a generalized Matrix and Vector interface that allows multiple matrix representations to be used with the same numerical algorithms.

The framework separates **matrix storage** from **numerical computation**, allowing algorithms to operate independently of the underlying matrix representation.

The implemented backends are:

- Dense Matrix
- CSR (Compressed Sparse Row) Matrix
- Banded Matrix
- Block Matrix

The project also includes matrix-vector operations, transpose operations, iterative numerical algorithms, cross-backend correctness testing, and performance measurement.

---

## Key Features

- Common abstract `Matrix` interface
- `Vector` implementation
- Dense matrix representation
- CSR sparse matrix representation
- Banded matrix representation
- Block matrix representation
- Element access using `get(i, j)`
- Matrix-vector multiplication
- Matrix transpose
- Python `@` operator support
- Power Iteration
- Jacobi Iterative Solver
- Cross-backend correctness testing
- Performance benchmarking
- Large-scale sparse/banded matrix testing

---

## Architecture

The project follows a backend-independent design:

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
              Common Numerical Algorithms
                           │
              ┌────────────┴────────────┐
              │                         │
       Power Iteration          Jacobi Solver
