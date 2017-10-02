# N_Queens_Problem

Backtracking:

The N queens problem is the problem of placing N non-attacking queens on an NxN chessboard, for which solutions exist for all natural numbers N with the exception of N=2 and N=3.

When N=1, the solution is trivial so the program will ask for a value of N such that N >= 4.

There are more efficient ways to solve this problem, but I will use backtracking since it’s the most intuitive way to arrive at the solution without getting into the mathematics of arriving at efficient solutions. Through solving these problems, I aim to better understand Python.

What is backtracking?

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons each partial candidate c (“backtracks”) as soon as it determines that c cannot possibly be completed to a valid solution.

A overview of how to use backtracking to solve the N queens problem:

    place a queen in the first column and first row
    place a queen in the second column such that it does not attack the queen in the first column
    continue placing non-attacking queens in the remaining columns
    if all N queens have been placed, a solution has been found. Remove the queen in the Nth column, and try incrementing the row of the       queen in the (N-1)th column
    if it’s a dead end, remove the queen, increment the row of the queen in the previous column
    continue doing this until the queen in the 1st column exhausts all options and is in the row N
