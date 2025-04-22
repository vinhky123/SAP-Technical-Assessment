"""
Problem: Write a function that counts the occurrences of each character in a string and returns a
map of characters to their respective counts.
Example:
Input: "sapstar"
Output: {s=2, a=2, p=1, t=1, r=1}

Approach: Similar to the problem 1, we need to use a for statement to loop through the string to build a hashmap with the dictionary data type in Python.
Finally, format the dictionary into a string with the format {key=value, ...}.
"""


def count_occurrences(s: str):
    # initialize the data structure
    count_map = {}

    # loop through the string to build a hashmap
    for char in s:
        if char in count_map:  # if it existed
            count_map[char] += 1

        else:  # if not
            count_map[char] = 1

    # create a list with format: char=count, for ex: ["s=2", "a=2", "p=1", "t=1", "r=1"]
    count_list = [f"{char}={count_map[char]}" for char in count_map]

    # use ", ".join function to connect elements of the count list with a comma between them, then wrap in braces
    return "{" + ", ".join(count_list) + "}"


if __name__ == "__main__":
    print("Input format: This is an example string \nThen hit Enter")
    input = str(input("Type Input string: "))

    output = count_occurrences(input)

    print(output)
