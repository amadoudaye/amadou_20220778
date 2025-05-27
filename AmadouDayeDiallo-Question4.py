# Open the input file to read and the output file to write
try:
    with open("data.txt", "r") as infile:
        lines = infile.readlines()

    # Filter lines containing 'error' (case-insensitive)
    error_lines = [line for line in lines if "error" in line.lower()]

    # Print each matching line
    for line in error_lines:
        print(line.strip())

    # Write the matching lines to 'errors.log'
    with open("errors.log", "w") as outfile:
        outfile.writelines(error_lines)

    # Print the count of matching lines
    print("Number of lines containing 'error':", len(error_lines))

except FileNotFoundError:
    print("The file 'data.txt' was not found.")