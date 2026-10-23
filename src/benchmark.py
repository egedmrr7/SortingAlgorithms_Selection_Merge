"""
Comparative Benchmark Suite: Selection Sort vs. Merge Sort
Course: Algorithm Analysis (2019G3009)
Lecturer: Dr. Coşkun Şahin
Student: Egemen Demir (ID: 2322190017)
"""

import time
import random
import tracemalloc
from typing import List, Tuple
from selection_sort import selection_sort, measure_memory_kb as mem_sel_kb
from merge_sort import merge_sort, measure_memory_kb as mem_merge_kb


def count_merge_comps(arr: List[int]) -> int:
    """Helper to count comparisons in Merge Sort."""
    def _merge_c(left: List[int], right: List[int]) -> Tuple[List[int], int]:
        res = []
        i = j = 0
        c = 0
        while i < len(left) and j < len(right):
            c += 1
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res, c

    def _ms(a: List[int]) -> Tuple[List[int], int]:
        if len(a) <= 1:
            return a, 0
        m = len(a) // 2
        l, c1 = _ms(a[:m])
        r, c2 = _ms(a[m:])
        res, c3 = _merge_c(l, r)
        return res, c1 + c2 + c3

    _, comps = _ms(arr)
    return comps


def run_comparative_suite() -> None:
    sizes = [1000, 2500, 5000, 10000]
    print("\n" + "=" * 98, flush=True)
    print(f"{'COMPARATIVE PERFORMANCE SUITE: SELECTION SORT vs MERGE SORT':^98}", flush=True)
    print("=" * 98, flush=True)

    header = f"{'Size (n)':<9} | {'Sel Time (s)':<13} | {'Merge Time (s)':<14} | {'Speedup':<9} | {'Sel RAM (KB)':<12} | {'Merge RAM (KB)':<14} | {'Sel Comps':<11} | {'Merge Comps':<11}"
    print(header, flush=True)
    print("-" * 98, flush=True)

    for n in sizes:
        random.seed(100 + n)
        test_data = [random.randint(1, n * 10) for _ in range(n)]

        # Selection Sort Timing
        t0 = time.perf_counter()
        selection_sort(test_data)
        t_sel = time.perf_counter() - t0
        mem_sel = mem_sel_kb(test_data)
        comps_sel = n * (n - 1) // 2

        # Merge Sort Timing
        t0 = time.perf_counter()
        merge_sort(test_data)
        t_merge = time.perf_counter() - t0
        mem_merge = mem_merge_kb(test_data)
        comps_merge = count_merge_comps(test_data)

        speedup = t_sel / t_merge if t_merge > 0 else 0.0

        row = (
            f"{n:<9} | {t_sel:<13.5f} | {t_merge:<14.5f} | {speedup:<8.1f}x | "
            f"{mem_sel:<12.1f} | {mem_merge:<14.1f} | "
            f"{comps_sel:<11} | {comps_merge:<11}"
        )
        print(row, flush=True)

    print("=" * 98, flush=True)


if __name__ == "__main__":
    run_comparative_suite()
