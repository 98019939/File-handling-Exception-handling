# 3. The w mode

fh =  open("file.txt", 'wt')
fh.write("This is overwritten using 'w' mode in python .\n")
fh.write("Have a nice day!")

fh.close()

fh =  open("file2.txt", 'wt')
fh.write("This is written using 'w' mode in python .\n")
fh.write("Have a nice day!")

fh.close()

# 4. Reading files
# file_handler = open("pratice.txt", 'rt')
# file_handler.read()
# print(file_handler)

# file_handler.close()
# 5. Appending into a file

fh = open("file.txt", 'at')
fh.write("\nthis content has been written using 'a' mode.\n")
fh.write("'a' mode is used to add new content at the end of the file.\n")
fh.write("Good bye")
fh.close()

# 6. The with statement

# with open("pratice.txt", 'xt') as fh:
#     contents = fh.read()
    
# print(contents)


with open("pratice_2.txt", 'xt') as fh:
    
    fh.write("New file creation\n")
    
    fh.write("Bye")