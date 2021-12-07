# Challenge Summary

Write a quick sort function that sorts an array in the quick sort way

## Whiteboard Process

![whiteboard](img/code-challenge-28.jpg)

## Approach & Efficiency

The approach of functions was used.

Big O:

* Time: O(nlogn)
* Time: O(n)

## Solution

    def QuickSort(arr, left, right):
        if left < right:
            position = Partition(arr, left, right)
            QuickSort(arr, left, position - 1)
            QuickSort(arr, position + 1, right)

        return arr

        def Partition(arr, left, right):
        pivot = arr[right]
        low = left - 1
        for i in range(left, right):
            if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)
        swap(arr, right, low + 1)
        return low +1


        def swap(arr, i, low):
        temp = arr[i]
        arr[i] = arr[low]
        arr[low] = temp

