print('File Testing for opening / closing / reading to and from files.')

myfile = open('myfile.txt', 'w')
# This creates a file object to the place where the Python directory is. myfile is a variable. 'w' is writing to the file. Open will open the file specified within the strings, if there is no file with the name within the strings then python will create a file with the name provided within the strings.

myfile.write('Hello text file\n')
# Writing to the text file with the string, then go to next line using\n

myfile.write('Goodbye text file\n')
#Write another line in the text file, then go to next line using \n

myfile.close()
# closes the file if open, and flushes the output buffers to disk.

myfile.open('myfile.txt')
# Opens the .txt file with the name myfile. here 'r' is by default so we do not need to explicitly write it.

myfile.readline()
# read line by line within the file. remember that myfile is a variable pointing to the File object.

myfile.readline()
# read it twice since we have two lines within the document.

myfile.readline() 
# when an empty string is returned it's the end of the file.

open('myfile.txt').read()
# Read the entiure file all at once into a single string, this includes all spaces and \n.

# A Better way to read the file is to uise the print function for a user friendly display 
print(open('myfile.txt').read())
# This will display the text in each line (as long as there is a \n in the text file.) This display does not display the \n like it did in the previous example.

# The best way to read a file is to use file iterators.
for line in open('myfile.txt'):
	print(line, end='')

# here line is a variable, remember that myfile variable has a 'w' write, not a defualt read so we cannot use that here unless we redefine the variaible. the open file object will iterate line by line through each iteration python knows to do the file iteration by itself within the iterator.