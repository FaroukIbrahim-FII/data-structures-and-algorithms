# Challenge Summary

Write a function that return an array sorted.

## Whiteboard Process

![whiteboard](img/code-challenge-26.jpg)

## Approach & Efficiency

The approach of creating a function was used.

Big O:

Time: O(n^2)
space: O(n)

## Solution

def insertionSort(arr:list[int]) :
    list_range = len(arr)
    for i in range(1, list_range):
        j = i - 1
        temp = i
        while j >= 0 and arr[j] > arr[temp]:
            pre = arr[j]
            current = arr[temp]
            arr[j] = current
            arr[temp] = pre
            j = j - 1
            temp -= 1

    return arr
