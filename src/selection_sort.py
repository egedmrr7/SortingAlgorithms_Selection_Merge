"""
Selection Sort Implementation and Performance Benchmark
Course: Algorithm Analysis (2019G3009)
Faculty of Engineering and Architecture / Software Engineering
Lecturer: Dr. Coşkun Şahin
Student: Egemen Demir (ID: 2322190017)
"""

import time
import random
import tracemalloc
from typing import List, Tuple


def selection_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array in ascending order using Selection Sort algorithm.
    Optimized for execution performance during benchmarking.
    """
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


def trace_selection_sort(arr: List[int]) -> None:
    """
    Prints a detailed step-by-step trace of the Selection Sort process.
    """
    a = arr.copy()
    n = len(a)
    print("=" * 70)
    print("SELECTION SORT STEP-BY-STEP TRACE")
    print(f"Initial Array: {a}")
    print("=" * 70)

    total_comparisons = 0
    total_swaps = 0

    for i in range(n - 1):
        min_idx = i
        step_comparisons = 0
        for j in range(i + 1, n):
            step_comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            old_val, new_val = a[i], a[min_idx]
            a[i], a[min_idx] = a[min_idx], a[i]
            total_swaps += 1
            action = f"Swap {old_val} (idx {i}) with {new_val} (idx {min_idx})"
        else:
            action = f"Element {a[i]} is already in place"

        total_comparisons += step_comparisons
        print(f"Pass {i + 1}: Min Found = {a[i]} | Comps: {step_comparisons} | {action}")
        print(f"        Sorted part: {a[:i+1]} | Unsorted part: {a[i+1:]}")
        print(f"        Array State: {a}\n")

    print(f"Final Sorted Array: {a}")
    print(f"Total Comparisons : {total_comparisons} [Formula n(n-1)/2 = {n*(n-1)//2}]")
    print(f"Total Swaps       : {total_swaps}")
    print("=" * 70)


def measure_memory_kb(arr: List[int]) -> float:
    """Measures peak auxiliary memory allocated during sort in KB."""
    tracemalloc.start()
    selection_sort(arr)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024.0


def run_benchmarks() -> None:
    """
    Benchmarks Selection Sort across various input sizes and patterns:
    - Best Case: Already sorted array
    - Worst Case: Reverse sorted array
    - Average Case: Randomly shuffled array
    """
    sizes = [1000, 2500, 5000, 10000]
    print("\n" + "=" * 80, flush=True)
    print("SELECTION SORT PERFORMANCE BENCHMARK (Time in seconds & Peak RAM in KB)", flush=True)
    print("=" * 80, flush=True)
    print(f"{'Size (n)':<10} | {'Best Case (s)':<15} | {'Worst Case (s)':<15} | {'Average Case (s)':<15} | {'Peak RAM (KB)':<12}", flush=True)
    print("-" * 80, flush=True)

    for n in sizes:
        # Best Case: already sorted
        best_arr = list(range(n))
        start = time.perf_counter()
        selection_sort(best_arr)
        best_time = time.perf_counter() - start

        # Worst Case: reverse sorted
        worst_arr = list(range(n, 0, -1))
        start = time.perf_counter()
        selection_sort(worst_arr)
        worst_time = time.perf_counter() - start

        # Average Case: random array
        random.seed(42)
        avg_arr = [random.randint(1, n * 10) for _ in range(n)]
        start = time.perf_counter()
        selection_sort(avg_arr)
        avg_time = time.perf_counter() - start

        # Memory profiling
        peak_kb = measure_memory_kb(avg_arr)

        print(f"{n:<10} | {best_time:<15.6f} | {worst_time:<15.6f} | {avg_time:<15.6f} | {peak_kb:<12.2f}", flush=True)

    print("=" * 80, flush=True)


if __name__ == "__main__":
    demo_array = [48, 12, 79, 35, 91, 24, 60, 17]
    trace_selection_sort(demo_array)
    run_benchmarks()
