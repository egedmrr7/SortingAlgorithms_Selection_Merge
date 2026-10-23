# ISTANBUL ESENYURT UNIVERSITY
## Faculty of Engineering and Architecture
### Department of Software Engineering (English)

---

# Midterm Project Report: Algorithm Analysis (2019G3009)
## Comparative Theoretical and Empirical Evaluation of Selection Sort and Merge Sort

| Field | Details |
| :--- | :--- |
| **Course Code & Name** | 2019G3009 — Algorithm Analysis |
| **Academic Term** | 2025–2026 Fall Semester |
| **Lecturer** | Dr. Coşkun Şahin |
| **Student Name Surname** | Egemen Demir |
| **Student Number** | 2322190017 |

---

## 1. Executive Summary & Overview

Sorting algorithms constitute one of the foundational subjects of computer science and algorithm design. Choosing an optimal sorting strategy requires a comprehensive evaluation of time complexity, auxiliary memory consumption, hardware cache locality, algorithm stability, and the cost of primary memory write operations.

This report presents an exhaustive comparative analysis of two contrasting sorting algorithms:
1. **Selection Sort:** An intuitive, comparison-based greedy algorithm that operates strictly in-place ($O(1)$ auxiliary space) and minimizes memory writes ($O(n)$ swaps), but exhibits an invariant quadratic time complexity ($\Theta(n^2)$).
2. **Merge Sort:** A classic divide-and-conquer algorithm that guarantees an optimal asymptotic time bound of $\Theta(n \log n)$ across all input distributions, achieved at the cost of $O(n)$ auxiliary memory for merging sub-arrays.

Both algorithms have been implemented from scratch in **Python 3**, mathematically analyzed, tested on an identical 8-element dataset (`[48, 12, 79, 35, 91, 24, 60, 17]`) for step-by-step verification, and benchmarked against standardized input distributions ranging from $n = 1,000$ to $n = 50,000$.

---

## 2. Selection Sort Analysis

### 2.1 Algorithm Overview and Mechanics

Selection Sort is an in-place comparison sort. It logically partitions the target list into two contiguous regions:
1. A **sorted prefix** on the left (initially empty).
2. An **unsorted suffix** on the right (initially containing the entire array).

During each iteration $i$ (from $0$ to $n - 2$), the algorithm scans the entire unsorted suffix to locate the index of the absolute minimum element. Once identified, this minimum element is swapped with the element at position $i$. Consequently, the boundary of the sorted prefix expands to the right by exactly one element per pass.

#### Pseudocode
```text
SELECTION-SORT(A, n):
    for i = 0 to n - 2:
        min_idx = i
        for j = i + 1 to n - 1:
            if A[j] < A[min_idx]:
                min_idx = j
        if min_idx != i:
            SWAP(A[i], A[min_idx])
```

### 2.2 Step-by-Step Execution Trace (Sample Walkthrough)

To ensure direct pedagogical comparability, both algorithms in this report are demonstrated on the exact same array:
$$\text{Initial Array: } A = [48, 12, 79, 35, 91, 24, 60, 17] \quad (n = 8)$$

| Pass ($i$) | Range Scanned | Minimum Found | Comparisons | Swap Action | Array State After Pass |
| :---: | :---: | :---: | :---: | :--- | :--- |
| **1** | $A[1 \dots 7]$ | $12$ (at idx 1) | 7 | Swap $A[0]=48$ with $A[1]=12$ | $[\mathbf{12}, 48, 79, 35, 91, 24, 60, 17]$ |
| **2** | $A[2 \dots 7]$ | $17$ (at idx 7) | 6 | Swap $A[1]=48$ with $A[7]=17$ | $[\mathbf{12}, \mathbf{17}, 79, 35, 91, 24, 60, 48]$ |
| **3** | $A[3 \dots 7]$ | $24$ (at idx 5) | 5 | Swap $A[2]=79$ with $A[5]=24$ | $[\mathbf{12}, \mathbf{17}, \mathbf{24}, 35, 91, 79, 60, 48]$ |
| **4** | $A[4 \dots 7]$ | $35$ (at idx 3) | 4 | No swap ($35$ already at index 3) | $[\mathbf{12}, \mathbf{17}, \mathbf{24}, \mathbf{35}, 91, 79, 60, 48]$ |
| **5** | $A[5 \dots 7]$ | $48$ (at idx 7) | 3 | Swap $A[4]=91$ with $A[7]=48$ | $[\mathbf{12}, \mathbf{17}, \mathbf{24}, \mathbf{35}, \mathbf{48}, 79, 60, 91]$ |
| **6** | $A[6 \dots 7]$ | $60$ (at idx 6) | 2 | Swap $A[5]=79$ with $A[6]=60$ | $[\mathbf{12}, \mathbf{17}, \mathbf{24}, \mathbf{35}, \mathbf{48}, \mathbf{60}, 79, 91]$ |
| **7** | $A[7 \dots 7]$ | $79$ (at idx 6) | 1 | No swap ($79$ already at index 6) | $[\mathbf{12}, \mathbf{17}, \mathbf{24}, \mathbf{35}, \mathbf{48}, \mathbf{60}, \mathbf{79}, \mathbf{91}]$ |

- **Total Comparisons:** $7 + 6 + 5 + 4 + 3 + 2 + 1 = \mathbf{28}$
- **Total Memory Swaps:** $\mathbf{5}$ swaps (Passes 4 and 7 did not require swaps)
- **Theoretical Formula Check:** $\frac{n(n - 1)}{2} = \frac{8 \times 7}{2} = 28$ comparisons.

---

### 2.3 Mathematical Complexity Analysis

#### 1. Time Complexity (CPU Workload)
The primary computational workload of Selection Sort arises from key comparisons performed in the nested loop. Regardless of whether the initial array is sorted, reverse-sorted, or randomly shuffled, the outer loop executes $n - 1$ times and the inner loop always runs $n - 1 - i$ times.

The exact total number of comparisons $C(n)$ is:
$$C(n) = \sum_{i=0}^{n-2} (n - 1 - i) = (n - 1) + (n - 2) + \dots + 2 + 1 = \frac{n(n - 1)}{2} = \frac{1}{2}n^2 - \frac{1}{2}n$$

- **Best-Case Time Complexity:** $\mathbf{\Theta(n^2)}$. Even if the array is already sorted, the algorithm has no early-exit mechanism; it must inspect every remaining element to confirm the minimum.
- **Worst-Case Time Complexity:** $\mathbf{\Theta(n^2)}$. When the array is reverse-sorted, the comparison count remains identically $\frac{n(n-1)}{2}$.
- **Average-Case Time Complexity:** $\mathbf{\Theta(n^2)}$. For uniform random permutations, the comparison count is invariant.

#### 2. Space Complexity (Memory Workload)
- **Auxiliary Space:** $\mathbf{O(1)}$. Selection Sort is an **in-place** sorting algorithm. It requires only three scalar pointer/index variables (`i`, `j`, `min_idx`) and a single temporary scalar for swapping. No dynamic heap allocation is incurred.
- **Memory Writes (Swaps):** At most $n - 1$ swaps are executed throughout the entire sorting process. This constitutes an asymptotic write bound of $\mathbf{O(n)}$, which is strictly superior to Bubble Sort ($O(n^2)$ writes) and Insertion Sort ($O(n^2)$ data shifts).

#### 3. Stability
- **Stability Status:** **Unstable**.
- **Explanation & Counterexample:** Selection Sort can shift an element past an equal key during a distant swap. Consider sorting pairs by their numeric key:
  $$A = [(2_a, \text{"red"}), (2_b, \text{"blue"}), (1, \text{"green"})]$$
  In pass 1, the minimum is $(1, \text{"green"})$ at index 2. It is swapped with $(2_a, \text{"red"})$ at index 0:
  $$A' = [(1, \text{"green"}), (2_b, \text{"blue"}), (2_a, \text{"red"})]$$
  The original relative order between $2_a$ and $2_b$ is inverted, proving non-stability.

---

### 2.4 Empirical Benchmark Results (Selection Sort)

Tests were executed using Python 3.13 on an AMD Ryzen 7 processor. High-resolution CPU timestamps (`time.perf_counter()`) and peak memory tracing (`tracemalloc`) were recorded:

| Input Size ($n$) | Best Case (s) | Worst Case (s) | Average Case (s) | Peak Auxiliary RAM (KB) |
| :---: | :---: | :---: | :---: | :---: |
| **1,000** | 0.035256 | 0.039912 | 0.038394 | 8.07 KB |
| **2,500** | 0.214818 | 0.228251 | 0.213223 | 19.79 KB |
| **5,000** | 0.926266 | 0.919021 | 0.873083 | 39.32 KB |
| **10,000** | 3.559393 | 3.694264 | 3.530147 | 78.39 KB |

> **Key Observation:** Across all input sizes, the execution times for Best, Worst, and Average cases are virtually identical (e.g., at $n = 10,000$, times are $3.55\text{s}$, $3.69\text{s}$, and $3.53\text{s}$). When $n$ quadruples from $2,500$ to $10,000$ (a $4\times$ increase), the runtime increases by approximately $16.5\times$ ($0.213\text{s} \times 16 \approx 3.4\text{s}$), empirically confirming the theoretical $\Theta(n^2)$ curve.

---

## 3. Merge Sort Analysis

### 3.1 Algorithm Overview and Mechanics

Merge Sort is a quintessential **Divide-and-Conquer** recursive algorithm invented by John von Neumann in 1945. It breaks down the problem through three systematic phases:
1. **Divide:** Compute the midpoint index $\lfloor n / 2 \rfloor$ and divide the sequence into two sub-sequences of sizes $\lfloor n / 2 \rfloor$ and $\lceil n / 2 \rceil$.
2. **Conquer:** Recursively sort each sub-sequence until the base case ($|A| \le 1$) is reached.
3. **Combine (Merge):** Linearly merge the two sorted sub-sequences into a single sorted array by iteratively picking the smaller head element.

#### Pseudocode
```text
MERGE-SORT(A):
    if length(A) <= 1:
        return A
    mid = length(A) // 2
    left_sorted = MERGE-SORT(A[0 ... mid - 1])
    right_sorted = MERGE-SORT(A[mid ... n - 1])
    return MERGE(left_sorted, right_sorted)

MERGE(left, right):
    result = []
    i = 0, j = 0
    while i < length(left) and j < length(right):
        if left[i] <= right[j]:    # <= preserves stability
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

### 3.2 Step-by-Step Execution Trace (Sample Walkthrough)

Using the **identical sample dataset** $A = [48, 12, 79, 35, 91, 24, 60, 17]$ ($n = 8 = 2^3$), the recursion tree decomposes symmetrically into $3$ levels of division and $3$ levels of merging:

```text
                                [48, 12, 79, 35, 91, 24, 60, 17]
                                       /                \
                       [48, 12, 79, 35]                  [91, 24, 60, 17]
                         /          \                      /          \
                   [48, 12]        [79, 35]          [91, 24]        [60, 17]
                    /    \          /    \            /    \          /    \
                 [48]    [12]    [79]    [35]      [91]    [24]    [60]    [17]   <- Base Cases
```

#### Detailed Merge Trace

1. **Leaf Merges (Level 1):**
   - $\text{Merge}([48], [12]) \implies [12, 48]$ (1 comparison: $48 > 12$)
   - $\text{Merge}([79], [35]) \implies [35, 79]$ (1 comparison: $79 > 35$)
   - $\text{Merge}([91], [24]) \implies [24, 91]$ (1 comparison: $91 > 24$)
   - $\text{Merge}([60], [17]) \implies [17, 60]$ (1 comparison: $60 > 17$)
   - *Level 1 comparisons:* $1 + 1 + 1 + 1 = 4$ comparisons.

2. **Intermediate Merges (Level 2):**
   - $\text{Merge}([12, 48], [35, 79])$:
     - Compare $12 \le 35 \to [12]$
     - Compare $48 > 35 \to [12, 35]$
     - Compare $48 \le 79 \to [12, 35, 48]$
     - Append remaining $79 \to [12, 35, 48, 79]$ (3 comparisons)
   - $\text{Merge}([24, 91], [17, 60])$:
     - Compare $24 > 17 \to [17]$
     - Compare $24 \le 60 \to [17, 24]$
     - Compare $91 > 60 \to [17, 24, 60]$
     - Append remaining $91 \to [17, 24, 60, 91]$ (3 comparisons)
   - *Level 2 comparisons:* $3 + 3 = 6$ comparisons.

3. **Final Root Merge (Level 3):**
   - $\text{Merge}([12, 35, 48, 79], [17, 24, 60, 91])$:
     - $12 \le 17 \to [12]$ (Comp 1)
     - $35 > 17 \to [12, 17]$ (Comp 2)
     - $35 > 24 \to [12, 17, 24]$ (Comp 3)
     - $35 \le 60 \to [12, 17, 24, 35]$ (Comp 4)
     - $48 \le 60 \to [12, 17, 24, 35, 48]$ (Comp 5)
     - $79 > 60 \to [12, 17, 24, 35, 48, 60]$ (Comp 6)
     - $79 \le 91 \to [12, 17, 24, 35, 48, 60, 79]$ (Comp 7)
     - Append remaining $91 \to [\mathbf{12, 17, 24, 35, 48, 60, 79, 91}]$
   - *Level 3 comparisons:* 7 comparisons.

- **Total Comparisons Across Entire Sort:** $4 + 6 + 7 = \mathbf{17}$ comparisons.
- **Comparison Comparison:** Merge Sort sorted this sequence with only **17 comparisons**, compared to Selection Sort which required **28 comparisons** (a $39.3\%$ reduction on just 8 elements!).

---

### 3.3 Mathematical Complexity Analysis

#### 1. Time Complexity (CPU Workload)
The runtime of Merge Sort is governed by the recurrence relation:
$$T(n) = 2T(n/2) + \Theta(n) \quad \text{for } n > 1, \quad T(1) = \Theta(1)$$

Where:
- $2T(n/2)$ represents the time required to recursively sort the two halves.
- $\Theta(n)$ represents the linear time required to merge the two sorted halves of size $n/2$.

**Solution via Master Theorem:**
The recurrence fits the standard form $T(n) = aT(n/b) + f(n)$ with $a = 2$, $b = 2$, and $f(n) = \Theta(n)$.
- Critical exponent: $\log_b a = \log_2 2 = 1$.
- Since $f(n) = \Theta(n^1) = \Theta(n^{\log_b a})$, this falls precisely into **Case 2 of the Master Theorem**.
- Therefore:
  $$T(n) = \Theta(n^{\log_b a} \log n) = \mathbf{\Theta(n \log_2 n)}$$

**Recursion Tree Perspective:**
- The recursion tree has a height of $\lceil \log_2 n \rceil + 1$.
- At depth $k$ ($0 \le k \le \log_2 n$), there are $2^k$ subproblems, each of size $n / 2^k$.
- The work done at level $k$ is $2^k \times c(n / 2^k) = c \cdot n$.
- Summing across all $\log_2 n$ levels yields:
  $$T(n) = \sum_{k=0}^{\log_2 n} c \cdot n = c \cdot n \cdot (\log_2 n + 1) = \mathbf{\Theta(n \log n)}$$

Because the merge step always processes the lists linearly and the recursion depth is strictly logarithmic, Merge Sort exhibits $\mathbf{\Theta(n \log n)}$ in **Best, Average, and Worst cases**.

#### 2. Space Complexity (Memory Workload)
- **Auxiliary Array Memory:** $\mathbf{O(n)}$. The standard merge subroutine cannot merge two arbitrary contiguous sub-arrays in-place in linear time. It requires an auxiliary buffer of size $n$ to hold merged elements before copying back.
- **Call Stack Memory:** $\mathbf{O(\log n)}$. The maximum depth of the active recursion call stack is bounded by the height of the binary recursion tree ($\lceil \log_2 n \rceil$).
- **Overall Space Complexity:** $\mathbf{O(n)}$.

#### 3. Stability
- **Stability Status:** **Stable**.
- **Explanation:** In the merge step, when elements from the left and right subarrays are equal (`left[i] == right[j]`), the algorithm explicitly selects `left[i]` (`left[i] <= right[j]`). Because `left[i]` preceded `right[j]` in the original array, their relative order is strictly preserved.

---

### 3.4 Empirical Benchmark Results (Merge Sort)

Benchmark results for Merge Sort executed under the same environment:

| Input Size ($n$) | Best Case (s) | Worst Case (s) | Average Case (s) | Peak Auxiliary RAM (KB) |
| :---: | :---: | :---: | :---: | :---: |
| **1,000** | 0.003276 | 0.002155 | 0.002982 | 16.90 KB |
| **2,500** | 0.005872 | 0.005689 | 0.011030 | 42.41 KB |
| **5,000** | 0.013396 | 0.011854 | 0.017105 | 82.05 KB |
| **10,000** | 0.025653 | 0.024763 | 0.035866 | 164.99 KB |
| **25,000** | 0.068232 | 0.069445 | 0.102785 | 424.68 KB |
| **50,000** | 0.144709 | 0.137282 | 0.210940 | 861.84 KB |

> **Key Observation:** Merge Sort executes $n = 50,000$ elements in just **0.21 seconds**, whereas Selection Sort would require over **90 seconds** for the same size! The peak memory grows strictly linearly with $n$ ($\approx 17\text{ KB}$ per 1,000 integers).

---

## 4. Comparative Evaluation

### 4.1 Side-by-Side Empirical Performance Suite

The following table presents head-to-head empirical metrics captured using `src/benchmark.py` running on identical randomized input arrays:

| Size ($n$) | Selection Sort Time (s) | Merge Sort Time (s) | Measured Speedup Factor | Selection Sort RAM (KB) | Merge Sort RAM (KB) | Selection Sort Comparisons | Merge Sort Comparisons | Comparison Ratio |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1,000** | 0.03648 s | 0.00302 s | **12.1x** | 8.1 KB | 16.9 KB | 499,500 | 8,690 | **57.5x** |
| **2,500** | 0.22213 s | 0.00810 s | **27.4x** | 19.8 KB | 42.4 KB | 3,123,750 | 25,126 | **124.3x** |
| **5,000** | 0.84385 s | 0.01681 s | **50.2x** | 39.3 KB | 82.0 KB | 12,497,500 | 55,196 | **226.4x** |
| **10,000** | 3.82775 s | 0.03604 s | **106.2x** | 78.4 KB | 165.0 KB | 49,995,000 | 120,378 | **415.3x** |

```
Execution Time Scaling Comparison (Log-Log Intuition):
Selection Sort: 0.036s -> 0.222s -> 0.844s -> 3.828s  [Quadratic Curve ~ O(n^2)]
Merge Sort    : 0.003s -> 0.008s -> 0.017s -> 0.036s  [Linearithmic Curve ~ O(n log n)]
```

---

### 4.2 Comprehensive Attribute Comparison Matrix

| Algorithmic Dimension | Selection Sort | Merge Sort | Significance in Engineering |
| :--- | :--- | :--- | :--- |
| **Algorithmic Paradigm** | Incremental Greedy Search | Divide and Conquer | Merge Sort parallelizes naturally; Selection Sort does not. |
| **Best-Case Time** | $\Theta(n^2)$ | $\Theta(n \log n)$ | Merge Sort is dramatically faster on large data. |
| **Average-Case Time** | $\Theta(n^2)$ | $\Theta(n \log n)$ | At $n = 10,000$, Merge Sort is $>100\times$ faster. |
| **Worst-Case Time** | $\Theta(n^2)$ | $\Theta(n \log n)$ | Merge Sort guarantees predictable performance without degrading. |
| **Auxiliary Memory** | $\mathbf{O(1)}$ (In-place) | $\mathbf{O(n)}$ (Buffer array) | Selection Sort has minimal memory footprint. |
| **Call Stack Depth** | $O(1)$ | $O(\log n)$ | No stack overflow risk in Selection Sort. |
| **Memory Write Count** | $\mathbf{\le n - 1}$ swaps ($O(n)$) | $O(n \log n)$ writes | Selection Sort minimizes physical writes to memory media. |
| **Stability** | ❌ No | ✅ Yes | Merge Sort preserves equal keys (vital for multi-column sorting). |
| **Hardware Cache Locality** | Poor (distant jumps during swaps) | High during linear merge passes | Sequential merge streams prefetch well in L1/L2 caches. |
| **Linked List Suitability** | Poor | Exceptional ($O(1)$ extra space) | Merge Sort sorts linked lists without extra array allocation. |

---

### 4.3 Evaluation of Best Use Cases

#### When to Choose Selection Sort:
1. **Flash Memory and EEPROM Devices:** In embedded microcontrollers (such as automotive sensors or IoT devices), flash memory has a limited endurance cycle (e.g., 10,000 to 100,000 write cycles before physical sector failure). Selection Sort guarantees at most $n - 1$ write operations, making it superior to algorithms that shift elements repeatedly.
2. **Severely Constrained RAM:** In systems where auxiliary memory is virtually zero (e.g., bare-metal 8-bit microcontrollers with only a few hundred bytes of RAM), Selection Sort's $O(1)$ space requirement and zero recursive stack overhead ensure safe execution without memory faults.
3. **Very Small Input Sizes ($n < 20$):** Due to minimal function call overhead and simplicity, Selection Sort runs with negligible code size footprint.

#### When to Choose Merge Sort:
1. **Large Enterprise Data Processing:** For datasets exceeding thousands of records, Merge Sort's $O(n \log n)$ asymptotic guarantee avoids catastrophic quadratic slowdowns.
2. **Stable Multi-Key Sorting:** When sorting database tables by multiple attributes (e.g., sorting employees first by salary, then by department), Merge Sort preserves the relative ordering of previously sorted fields.
3. **External Sorting (Disk and Tape Drives):** When data exceeds main memory (RAM) capacity and resides on secondary storage, Merge Sort is the industry standard (e.g., in external tape merges and database query engines) because merging sequential disk streams requires only linear streaming buffers.
4. **Linked List Sorting:** Unlike arrays, linked lists can be split and merged by adjusting pointers in $O(1)$ space, making Merge Sort the optimal $O(n \log n)$ time and $O(1)$ auxiliary space choice for pointer-based lists.

---

## 5. Conclusion

This project evaluated Selection Sort and Merge Sort through theoretical derivations and empirical benchmarks:

1. **Empirical Validation of Asymptotics:** The benchmark results confirm that Selection Sort's runtime scales quadratically ($\approx 4\times$ increase for every $2\times$ increase in $n$), while Merge Sort scales almost linearly ($n \log n$). At $n = 10,000$, Merge Sort achieved a **106.2x speedup** while reducing comparison operations from $49,995,000$ to $120,378$ (a $415\times$ reduction).
2. **The Space-Time Trade-off:** Merge Sort achieves its speed advantage by trading space, requiring $O(n)$ auxiliary buffer memory ($165\text{ KB}$ at $n = 10,000$). Conversely, Selection Sort maintains strict in-place operation ($O(1)$ auxiliary memory).
3. **Memory Write Economy vs Comparison Economy:** Selection Sort remains relevant in domain-specific engineering scenarios where write operations to physical storage media are expensive or destructive, whereas Merge Sort dominates in general computing, database systems, and external sorting.

---

## 6. References

1. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2022). *Introduction to Algorithms* (4th ed.). MIT Press. Chapter 2 (Getting Started) & Chapter 4 (Divide-and-Conquer).
2. **Sedgewick, R., & Wayne, K.** (2011). *Algorithms* (4th ed.). Addison-Wesley Professional. Section 2.1 (Elementary Sorts) & Section 2.2 (Mergesort).
3. **Knuth, D. E.** (1998). *The Art of Computer Programming, Volume 3: Sorting and Searching* (2nd ed.). Addison-Wesley. Section 5.2.2 (Sorting by Exchanging) & Section 5.2.4 (Sorting by Merging).

---

## 7. AI Utilization Rules and Ethic Codes Statement

In strict compliance with the project guidelines established by Dr. Coşkun Şahin for the 2019G3009 Algorithm Analysis course, the following disclosure statement is declared:

> "Gemini 3.8 Flash (Google DeepMind) was used in the [Code generation, Performance Benchmarking, and Report Structuring] section of this product. The tool was utilized via the prompt/input "Generate Python implementations, step-by-step traces, empirical benchmarks, and comparative academic report for Selection Sort and Merge Sort" for the purpose of [Code generation / Algorithm editing / Documentation / Text correction]. The output generated has been reviewed and verified by me for technical accuracy, safety, and originality. I bear full responsibility for the work."
