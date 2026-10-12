# Python Math Projects

Small Python projects exploring number sequences, factors, and plotting.

| Script | What it does |
| --- | --- |
| [Common numbers in a set](python/common%20numbers%20in%20a%20set.py) | Counts values of `n` from 1 to 2004 where `4n` is divisible by 6. |
| [Arithmetic sequence rule](python/explicit%20rule%20of%20an%20arithmetic%20sequence.py) | Finds a linear rule from two known terms of an arithmetic sequence. |
| [Fibonacci sequence](python/fibonacci%20sequence.py) | Calculates Fibonacci terms using recursion and a stored list. |
| [Rising and falling sequence](python/printing%20a%20set-firstprgm.py) | Builds a sequence with increasing peaks and prints selected results. |
| [Prime factors](python/printing%20prime%20factors.py) | Experiments with generating primes and recursively factoring a number. |
| [Distinct prime factor plot](python/distinct_prime_factor_plot.py) | Plots the number of distinct prime factors for a range of numbers. Originally named `rohanscode.py`. |

## Run

Install Python 3, then run a script from the repository folder:

```sh
python "python/fibonacci sequence.py"
```

The plotting script also needs NumPy and Matplotlib:

```sh
python -m pip install -r requirements.txt
python python/distinct_prime_factor_plot.py
```

These are practice projects with values set in the source. The factorization scripts are experiments; their results have not been validated for all inputs.
