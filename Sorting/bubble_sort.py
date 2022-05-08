from typing import List


def bubble_sort(arr: List[int]):
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    bubble_sort(arr)
    print(arr)
