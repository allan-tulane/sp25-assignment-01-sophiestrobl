

# CMPS 2200 Assignment 1

**Name:** Sophie Strobl


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes, $2^{n+1} \in O(2^n) because it can be rewritten as 2 * 2^n. Setting the constant to 2 satisfies the big-O condition, proving the growth rate is at most a constant multiple of 2^n.
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No, 2^(2^n) is not in O(2^n) because it grows exponentially faster than 2^n. Rewriting the inequality 2^(2^n) ≤ c * 2^n and dividing both sides by 2^n gives 2^(2^n - n) ≤ c. Since 2^n grows exponentially, the exponent (2^n - n) also tends to infinity, causing 2^(2^n - n) to grow unbounded. This contradicts the idea of a constant c bounding the function, proving that 2^(2^n) is not in O(2^n).
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No, n^1.01 is not in O(log^2 n) because polynomial functions grow much faster than logarithmic functions. As n increases, n^1.01 grows significantly faster than log^2 n, making it impossible to find a constant that keeps n^1.01 smaller for all large values of n. Since no such constant exists, n^1.01 is not in O(log^2 n).
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes, n^1.01 is in Ω(log^2 n) because polynomial functions grow faster than logarithmic functions. Since n^1.01 increases much more rapidly than log^2 n, there will always be a point where n^1.01 is greater than any constant times log^2 n. This confirms that n^1.01 grows at least as fast as log^2 n, so it belongs to Ω(log^2 n).
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No, sqrt(n) is not in O((log n)^3) because polynomial functions grow faster than logarithmic functions. Sqrt(n) grows much faster than (log n)^3 as n increases. Since no constant can bound sqrt(n) by (log n)^3 for all large n, sqrt(n) is not in O((log n)^3).
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes, sqrt(n) is in omega((log n)^3) because polynomial functions grow faster than logarithmic functions. Since sqrt(n) grows much faster than (log n)^3, there will always be a point where sqrt(n) is greater than any constant times (log n)^3. This confirms that sqrt(n) grows at least as fast as (log n)^3, so it belongs to omega((log n)^3).


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  The function foo(x) computes the Fibonacci sequence recursively. The function generates the Fibonacci number at position x by summing the two previous numbers in the sequence. However, because it does not use memoization or iteration, it recalculates values multiple times, making it inefficient for large values of x.
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The Work of the iterative longest_run function is O(n) because it processes each element in the list once, performing a constant amount of work per iteration. The Span is also O(n) since the function executes sequentially, with each step depending on the previous one, preventing parallelization. This makes the algorithm efficient in total operations but not easily parallelizable.
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  The Work of longest_run_recursive is O(n) because it processes every element across recursive calls and merging steps. The Span is O(log n) since the recursion splits the list in half at each level. This makes the recursive approach more parallelizable than the iterative version, which had a span of O(n). 
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
.  When longest_run_recursive is parallelized by spawning new threads for each recursive call, the Work remains O(n) since every element is still processed. However, the Span improves to O(log n) because the recursive calls now execute in parallel, reducing the longest dependency chain. This makes the algorithm very parallelizable, allowing for near-linear speedup with enough processors.
.  
.  
.  
.  
.  
.  
.  

