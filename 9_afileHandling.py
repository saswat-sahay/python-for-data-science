# OPEN FUNCTION

# open('') - open function takes a url of the file 
# p = open('1_dataTypes_stringIndexing_stringSlicing_typeConversion_TruthyAndFalsyValues.py')
# p = open(r'1_dataTypes_stringIndexing_stringSlicing_typeConversion_TruthyAndFalsyValues.py')

# modes
'''
Mode    Description

‘r’     Read (default) – file must exist.

‘w’     Write – creates file or overwrites.

‘a’     Append – adds to end of file.

‘x’     Create – creates a new file, fails if it exists.
'''
File1 = open("heros.txt", "w")  # when we run this line we get a new file named heros.txt
# r is the default mode

# writing in a file

# w

# File1.write("This line is coming from write funciton from 9_fileHandling.py")
# if you want to add more contents to the original file then either you can use write multiple times else if you rewrite this upper line again like i did in the below line; then the file will gets overwrites
# File1.write(" I am adding this new line")
# see it removes the other content of the file and overwrites it
# if you were used 'a' instead of 'w'then this problem wont be happend

# a

File2 = open("append.txt", "a")
File2.write(". And i append this line also")
# we can see that we can write multiple lines in one single line
File1.close()
