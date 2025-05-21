def word_count(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Create an empty dictionary to store word counts
    word_dict = {}
    
    # Count each word
    for word in words:
        word = word.lower()  # Optional: make it case-insensitive
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    return word_dict

# Example input
input_sentence = "the cat and the dog"

# Get the word count dictionary
output = word_count(input_sentence)

# Print the result
print("Input:", input_sentence)
print("Output:", output)