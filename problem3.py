"""
Problem: Write a function that takes two sorted arrays of integers and merges them into a single
sorted array. The resulting array should also be sorted.
Example:
Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

This problem reminds me of the merge phase in the merge sort algorithm.

Approach: Use the two-pointer technique to iterate through both arrays, comparing elements at each pointer.
Add the smaller element to the result array and advance the corresponding pointer.
Append any remaining elements from either array to the result.
"""


def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    # Initialize pointers and result array
    i = 0  # first array's pointer
    N = len(arr1)

    j = 0  # second array's pointer
    M = len(arr2)

    result = []

    # while both of them has not reached the final number of their list
    while i < N and j < M:
        # make a comparation, whichever smaller will be added to the result list and move forward
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # add the remaining elements to result
    while i < N:
        result.append(arr1[i])
        i += 1
    while j < M:
        result.append(arr2[j])
        j += 1

    return result


if __name__ == "__main__":
    print("Input format: num1 num2 num3 num4 .... \nThen hit Enter")
    arr_1 = list(map(int, input("Type array 1: ").split()))
    arr_2 = list(map(int, input("Type array 2: ").split()))

    output = merge_sorted_arrays(arr_1, arr_2)

    print("Output: ", end="")
    print(output)
