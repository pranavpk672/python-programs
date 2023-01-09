# program to read file content and store it into a list.
# using readlines()

open_file = open('csvfile.csv', 'r')
File_Lines = open_file.readlines()

# without using strip
print("\nFile content with newline character: ")
print(File_Lines)

# By using strip
print("\nFile content after removing newline character:")
File_Lines = [X.strip() for X in File_Lines]
print([X.strip() for X in File_Lines])
open_file.close()

