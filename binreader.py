#binreader

# python file to read a simple text file containing binary code and output it's characters to the screen

# first we'll just set up the skeleton and print functions to remind ourselfs

# let's take some args and print out the name of the file entered

import sys
import io

print("Welcome to BinReader, hope you enjoy your stay")

#this should be the file indicated by the first CLI argument, no error checking for now
targetFile = sys.argv[1]
print("File to scan is", targetFile)

with open(targetFile, "r") as readFile:
    print(readFile.read())