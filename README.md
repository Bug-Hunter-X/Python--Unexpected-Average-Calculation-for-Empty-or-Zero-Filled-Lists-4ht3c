# Python: Handling Empty Lists and Zeros in Average Calculation

This repository showcases a common error in Python when calculating the average of a list: how to gracefully handle empty lists and lists containing only zeros.  The `bug.py` file demonstrates the problem, while `bugSolution.py` offers a refined solution.

**Problem:**
The initial `calculate_average` function returns 0 for both empty lists and lists filled with only zeros. While this might be acceptable in certain scenarios, it might lead to unexpected results and masking of errors in other contexts. A more robust solution is needed.

**Solution:**
The improved function in `bugSolution.py` raises exceptions for these edge cases, providing clearer error feedback and preventing potential issues. This allows the calling code to handle these situations appropriately.