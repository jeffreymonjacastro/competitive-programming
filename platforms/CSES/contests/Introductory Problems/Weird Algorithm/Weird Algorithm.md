---
platform: Cses
contest: Introductory Problems
difficulty: 800
status: 🟢Solved
date: 2025-07-30
tags:
  - cp
  - implementation
  - techniques
---
# [Weird Algorithm](https://cses.fi/problemset/task/1068)

## 📓 Related Topics
- [[topics/techniques/Implementation|Implementation]]

## 📖 Description
Given a positive integer n, the task is to generate the sequence defined by the following rules:
- If n is even, the next number is n / 2.
- If n is odd, the next number is 3 * n + 1.
The sequence ends when it reaches 1.

## 💡 Approach
Implement a loop that continues until n becomes 1. In each iteration, check if n is even or odd and update n accordingly. Print each value of n in the sequence.

## ⚡ Complexity
- **Time:** O(?)
- **Space:** O(1)

## 🔍 Key Points
- The sequence is known as the Collatz conjecture or 3n + 1 problem.
- The sequence always reaches 1 for any positive integer n.

## 🔗 Related Problems
- [Similar Problem 1]
- [Similar Problem 2]

## 🔄 Versions
- `solution.py` - Main solution 
