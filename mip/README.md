# Mixed Integer Programming

This is the task related to mixed integer programming (MIP) with package `Pulp` for Python.

## Steps

- sudo apt-get install python-pip
- python3.5 -m venv env
- source env/bin/activate
- python -m pip install --upgrade pip
- pip install pulp
- python index.py

Press `Ctrl + C` to close app, and run `deactivate` to leave virtual environment.

# Example 

Knapsack problem: given a set I of items, each one with a weight `wi` and estimated profit `vi`, one wants to select a subset with maximum profit such that the summation of the weights of the selected items is less or equal to the knapsack capacity `limit`. Considering a set of decision binary variables `xi` that receive value 1 if the i-th item is selected, or 0 if not.
