import codecs
import sys

my_file = sys.argv[1]


def cleaning(my_file):
    for lines in my_file:
        my_file.write(lines.strip())

while True:
    selection = raw_input("Please type 'N' to write to a new file or 'O' to write over the current file")

    if selection.lower() == "n":
        print "Making a new file without leading/trailing whitespace"
        newfile = codecs.open("%s_clean.txt" % str(my_file), 'w')
        cleaning(codecs.open(my_file))

    elif selection.lower() == "o":
        print "Deleting trailing/leading whitespace of he current file"
        cleanfile = codecs.open(my_file, 'r+')
        cleanfile.seek(0)
        cleaning(cleanfile)
    else:
        print "Please select a valid option"
