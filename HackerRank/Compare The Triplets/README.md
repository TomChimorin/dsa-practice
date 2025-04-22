# Compare The Triplets

This repository contains the solution for the "Compare The Triplets" problem from HackerRank.

## Problem Description

Alice and Bob each created three challenges. Each challenge is scored with an integer from 1 to 100. The task is to compare their scores for each challenge and award points:

If Alice's score is higher than Bob's, Alice gets 1 point.

If Bob's score is higher than Alice's, Bob gets 1 point.

If their scores are equal, neither gets a point.

Return the total score as a list: [Alice's score, Bob's score].

## Solution

The solution uses a loop to compare each element of the two input arrays a and b. At each index:

Compare the corresponding scores.

Increment Alice’s or Bob’s score based on who performed better.

Finally, the result is returned as a list containing both scores.

## How to Run

To run the solution:

1. Clone this repository to your local machine.
2. Run the Python file:

```bash
python compare_the_triplets.py
