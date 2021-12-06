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


# if __name__ == '__main__':
#     print(insertionSort([8, 4, 23, 42, 16, 15]))
