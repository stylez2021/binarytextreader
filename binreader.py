#binreader

#python file to read a simple text file containing binary code and output it's characters to the screen
#first we'll just set up the skeleton and print functions to remind ourselfs

import sys
import io
from bitarray import bitarray


print("Welcome to BinReader, hope you enjoy your stay")

#let's take some args and print out the name of the file entered
#this should be the file indicated by the first CLI argument, no error checking for now
targetFile = sys.argv[1]
print("File to scan is", targetFile)

#open up the file for use in python
with open(targetFile, "r") as readFile:
    fileText = (readFile.read())
    print(fileText.split())


# Ok now, I can print the list just to see it and make sure but this part isn't necessary, already printed above so commenting out.
#for i in fileText.split():
#    print(i)

#convert and print
bts = bitarray(fileText)
ASCS = bts.tobytes().decode('ascii')
print("\nThe message should be:\n")
print(ASCS + "\n")