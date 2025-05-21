def count_characters(text):
    # Create an empty dictionary to hold character counts
    char_count = {}

    # Loop through each character in the string
    for char in text:
        if char != ' ':  # Ignore spaces
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

# Example input
input_string = "hello world"

# Get the character count
output = count_characters(input_string)

# Print the result
print("Input:", input_string)
print("Output:", output)