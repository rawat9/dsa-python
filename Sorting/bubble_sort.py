from typing import List


def bubble_sort(arr: List[int]):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            break


if __name__ == "__main__":
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    bubble_sort(arr)
    print(arr)
