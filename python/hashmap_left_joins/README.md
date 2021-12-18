# Hashmap LEFT JOIN

The SQL LEFT JOIN returns all rows from the left table, even if there are no matches in the right table. This means that if the ON clause matches 0 (zero) records in the right table; the join will still return a row in the result, but with NULL in each column from the right table.

This means that a left join returns all the values from the left table, plus matched values from the right table or NULL in case of no matching join predicate.

## Challenge

Write a function that LEFT JOINs two hashmaps into a single data structure.

## Approach & Efficiency

The approach of creating a function were used

Big O:

* Time: O(n + m): where the n is the length of the first hash map and m is the length of the second hash map.
* Space: O(n): since we are creating a lists inside the function

## Solution

![whiteboard](img/Code-Challenge-33.jpg)

