# 1. Introduction to File handling


file_handeler = open("pratice.txt", "rt")
print(file_handeler)

file_handeler.close()

# 2. Creating files

fh = open("file.txt","xt")

fh.write("This file is created using 'x' mode in python \n")
fh.write("Next Line")

fh.close()



