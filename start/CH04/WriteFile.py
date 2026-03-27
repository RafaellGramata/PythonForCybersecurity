#!/usr/bin/env python3
# Sample script that writes to a file
# By Rafaell

# Open file for writing. Change "w" to "a" to append instead.
test_file = open("testfile.txt", "w")

# Write lines to the file
test_file.write("Hello World\n")
test_file.write("My name is Rafaell\n")
test_file.write("I like rubber ducks\n")

# Close the file
test_file.close()