# Comparative Analysis of Selection Sort and Merge Sort

**Course:** 2019G3009 Algorithm Analysis  
**Department:** Software Engineering (English)  
**Institution:** Istanbul Esenyurt University  
**Lecturer:** Dr. Coşkun Şahin  
**Student:** Egemen Demir (Student ID: 2322190017)  
**Submission:** Shared with `drcoskuns` as collaborator via GitHub  

---

## 📌 Project Overview

This repository contains the Midterm Project for the **Algorithm Analysis** course. The project delivers an in-depth theoretical and empirical comparison of two fundamental sorting algorithms:

1. **Selection Sort** — An in-place, non-stable comparison sort characterized by quadratic time complexity $O(n^2)$ and an optimal, strictly bounded number of memory writes ($O(n)$ swaps).
2. **Merge Sort** — A divide-and-conquer, stable comparison sort guaranteeing an optimal $O(n \log n)$ time complexity across all input distributions, utilizing $O(n)$ auxiliary memory.

Both algorithms are implemented from scratch in **Python 3.13+**, accompanied by step-by-step trace routines on identical test datasets, comprehensive asymptotic proofs, and empirical profiling across CPU runtime, memory allocation, and comparison counts.

---

## 📁 Repository Structure

```text
SortingAlgorithms_Selection_Merge/
├── README.md              # Project documentation and execution guide
├── REPORT.md              # Comprehensive academic midterm report (.md formatted)
└── src/
    ├── selection_sort.py  # Selection Sort implementation, trace, and benchmarks
    ├── merge_sort.py      # Merge Sort implementation, recursive trace, and benchmarks
    └── benchmark.py       # Comparative head-to-head benchmarking suite
```

---

## 🚀 How to Run the Code

### Prerequisites
- Python 3.8 or higher (No third-party packages required; built entirely with Python standard libraries `time`, `random`, `tracemalloc`, and `typing`).

### 1. Run Selection Sort (Step-by-Step Trace & Single Benchmark)
```bash
python src/selection_sort.py
```
*Outputs the step-by-step trace on the demo dataset `[48, 12, 79, 35, 91, 24, 60, 17]`, followed by benchmark times for Best, Worst, and Average cases up to $n = 10,000$.*

### 2. Run Merge Sort (Recursive Division Tree & Single Benchmark)
```bash
python src/merge_sort.py
```
*Outputs the visual divide-and-conquer recursion tree and merge passes on the demo dataset `[48, 12, 79, 35, 91, 24, 60, 17]`, followed by benchmark times up to $n = 50,000$.*

### 3. Run Head-to-Head Comparative Benchmark Suite
```bash
python src/benchmark.py
```
*Runs both algorithms simultaneously against identical random datasets from $n = 1,000$ to $n = 10,000$, measuring execution times, speedup factor, peak auxiliary RAM, and comparison counts.*

---

## 📊 Summary of Theoretical Complexity

| Property | Selection Sort | Merge Sort |
| :--- | :--- | :--- |
| **Best-Case Time Complexity** | $\Theta(n^2)$ | $\Theta(n \log n)$ |
| **Average-Case Time Complexity** | $\Theta(n^2)$ | $\Theta(n \log n)$ |
| **Worst-Case Time Complexity** | $\Theta(n^2)$ | $\Theta(n \log n)$ |
| **Auxiliary Space Complexity** | $O(1)$ (In-place) | $O(n)$ (Out-of-place buffer) |
| **Call Stack Depth** | $O(1)$ | $O(\log n)$ |
| **Stability** | ❌ No (Swaps skip intermediate elements) | ✅ Yes (Left element chosen on tie) |
| **Data Movement / Swaps** | $\le n - 1$ swaps ($O(n)$ writes) | $O(n \log n)$ writes |
| **Algorithmic Paradigm** | Incremental / Greedy Selection | Divide and Conquer |

For the complete theoretical proofs, memory hierarchy evaluation, empirical tables, and best use-case discussions, refer to [**REPORT.md**](REPORT.md).
