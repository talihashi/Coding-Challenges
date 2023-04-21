# https://replit.com/@JordanGent/Coding-Challenges

# Week 1: Basics and Data Structures

# Challenge 1: Write a program that takes two numbers as input and prints their sum.
def get_sum(num1, num2):
  print(num1 + num2)
# Challenge 2: Write a program that takes a string input and reverses it.
def reverse_string(string):
  print(string[::-1])
# Challenge 3: Write a program that checks if a given number is prime.
def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True
# Challenge 4: Write a program that takes a list of numbers and finds the maximum and minimum elements.
def find_max_min(num_list):
  num_list.sort()
  print(f"The max is {num_list[-1]}. The min is {num_list[0]}")
# Challenge 5: Write a program that removes duplicates from a given list.
def remove_duplicates(given_list):
   print(set(given_list))



# Week 2: Functions and Recursion

# Challenge 6: Write a recursive function to calculate the factorial of a number.

# Challenge 7: Write a function that takes a list and a target number and returns the indices of two numbers in the list that sum up to the target.

# Challenge 8: Write a recursive function to calculate the Fibonacci sequence up to a given number.

# Challenge 9: Write a program that takes a list of strings and sorts them alphabetically.



# Week 3: Object-Oriented Programming

# Challenge 10: Implement a class for a simple 2D point, with methods for calculating distance and midpoint between two points.

# Challenge 11: Implement a class for a bank account, with methods for depositing, withdrawing, and checking the balance.

# Challenge 12: Implement a class for a simple 2D rectangle, with methods for calculating area and perimeter.

# Challenge 13: Implement a class for a circle, with methods for calculating area and circumference.



# Week 4: File I/O and Exception Handling

# Challenge 14: Write a program that reads a text file and counts the number of lines, words, and characters in it.

# Challenge 15: Write a program that reads a CSV file and calculates the average value of a specific column.

# Challenge 16: Write a program that reads a JSON file and prints the data in a user-friendly format.

# Challenge 17: Write a program that catches and handles exceptions for common file I/O errors.



# Week 5: Algorithm Design and Optimization

# Challenge 18: Implement a binary search algorithm.

# Challenge 19: Implement a selection sort algorithm.

# Challenge 20: Implement a merge sort algorithm.

# Challenge 21: Implement a quicksort algorithm.



# Week 6: Advanced Data Structures

# Challenge 22: Implement a stack using a linked list.

# Challenge 23: Implement a queue using a linked list.

# Challenge 24: Implement a binary search tree.

# Challenge 25: Implement a trie for word search.



# Week 7: Graph Algorithms

# Challenge 26: Implement depth-first search (DFS) for a given graph.

# Challenge 27: Implement breadth-first search (BFS) for a given graph.

# Challenge 28: Implement Dijkstra's shortest path algorithm.

# Challenge 29: Implement a topological sort algorithm.



# Week 8: Dynamic Programming

# Challenge 30: Implement a dynamic programming solution for the Fibonacci sequence.

# Challenge 31: Implement a dynamic programming solution for the longest common subsequence problem.

# Challenge 32: Implement a dynamic programming solution for the 0/1 knapsack problem.

# Challenge 33: Implement a dynamic programming solution for the coin change problem.