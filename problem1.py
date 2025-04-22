"""
Problem: Write a function that takes a string and returns the first non-repeating character in the
string. If there are no non-repeating characters, return null

Example:
Input: "sapstar"
Output: "p"

Approach: Use a for statement to loop thourgh all characters of the string to build a hashmap in order to find out which character are repeating.
To handle this in Python, the data type called dictionary will be used.
Finally, iterate through the string again to find the first character with a count of 1.
"""


def first_non_repeating(s: str):
    # initialize the data structure
    count_map = {}

    # loop through the string to build a hashmap
    for char in s:
        if char in count_map:  # if it existed
            count_map[char] += 1

        else:  # if not
            count_map[char] = 1

    for char in s:  # iterate again
        if count_map[char] == 1:  # if it is a non-repeating character
            return char

    return "null"  # When the second loop is over but no character returned


if __name__ == "__main__":
    print("Input format: This is an example string \nThen hit Enter")
    input = str(input("Type Input: "))

    output = first_non_repeating(input)

    print("Output: " + output)
