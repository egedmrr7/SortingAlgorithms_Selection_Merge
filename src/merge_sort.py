"""
Merge Sort Implementation and Performance Benchmark
Course: Algorithm Analysis (2019G3009)
Faculty of Engineering and Architecture / Software Engineering
Lecturer: Dr. Coşkun Şahin
Student: Egemen Demir (ID: 2322190017)
"""

import time
import random
import tracemalloc
from typing import List, Tuple


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.
    Preserves stability (<= condition).
    """
    merged = []
    i = j = 0
    len_l, len_r = len(left), len(right)

    while i < len_l and j < len_r:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr: List[int]) -> List[int]:
    """
    Recursively sorts an array in ascending order using Merge Sort (Divide-and-Conquer).
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    return merge(left_sorted, right_sorted)


def trace_merge_sort(arr: List[int], depth: int = 0, side: str = "Root") -> Tuple[List[int], int]:
    """
    Demonstrates recursive division and merge steps with tree visualization.
    """
    indent = "   " * depth
    n = len(arr)
    print(f"{indent}--> [{side}] Split: {arr} (size={n})")

    if n <= 1:
        print(f"{indent}<-- [{side}] Base case: {arr}")
        return arr, 0

    mid = n // 2
    left_sorted, left_comps = trace_merge_sort(arr[:mid], depth + 1, "Left")
    right_sorted, right_comps = trace_merge_sort(arr[mid:], depth + 1, "Right")

    # Merge step with comparison counting
    merged = []
    i = j = 0
    merge_comps = 0
    while i < len(left_sorted) and j < len(right_sorted):
        merge_comps += 1
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])

    total_comps = left_comps + right_comps + merge_comps
    print(f"{indent}<-- [{side}] Merged: {left_sorted} + {right_sorted} ===> {merged} (Comps: {merge_comps})")
    return merged, total_comps


def measure_memory_kb(arr: List[int]) -> float:
    """Measures peak auxiliary memory allocated during sort in KB."""
    tracemalloc.start()
    merge_sort(arr)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024.0


def run_benchmarks() -> None:
    """
    Benchmarks Merge Sort across various input sizes and patterns:
    - Best Case: Already sorted array
    - Worst Case: Reverse sorted array
    - Average Case: Randomly shuffled array
    """
    sizes = [1000, 2500, 5000, 10000, 25000, 50000]
    print("\n" + "=" * 80, flush=True)
    print("MERGE SORT PERFORMANCE BENCHMARK (Time in seconds & Peak RAM in KB)", flush=True)
    print("=" * 80, flush=True)
    print(f"{'Size (n)':<10} | {'Best Case (s)':<15} | {'Worst Case (s)':<15} | {'Average Case (s)':<15} | {'Peak RAM (KB)':<12}", flush=True)
    print("-" * 80, flush=True)

    for n in sizes:
        # Best Case: already sorted
        best_arr = list(range(n))
        start = time.perf_counter()
        merge_sort(best_arr)
        best_time = time.perf_counter() - start

        # Worst Case: reverse sorted
        worst_arr = list(range(n, 0, -1))
        start = time.perf_counter()
        merge_sort(worst_arr)
        worst_time = time.perf_counter() - start

        # Average Case: random array
        random.seed(42)
        avg_arr = [random.randint(1, n * 10) for _ in range(n)]
        start = time.perf_counter()
        merge_sort(avg_arr)
        avg_time = time.perf_counter() - start

        peak_kb = measure_memory_kb(avg_arr)

        print(f"{n:<10} | {best_time:<15.6f} | {worst_time:<15.6f} | {avg_time:<15.6f} | {peak_kb:<12.2f}", flush=True)

    print("=" * 80, flush=True)


if __name__ == "__main__":
    demo_array = [48, 12, 79, 35, 91, 24, 60, 17]
    print("=" * 70)
    print("MERGE SORT STEP-BY-STEP RECURSIVE TRACE")
    print(f"Initial Array: {demo_array}")
    print("=" * 70)
    sorted_res, total_comps = trace_merge_sort(demo_array)
    print(f"\nFinal Sorted Array: {sorted_res}")
    print(f"Total Comparisons : {total_comps}")
    print("=" * 70)
    run_benchmarks()
