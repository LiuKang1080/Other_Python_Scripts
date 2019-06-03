while True:
	reply = input('Enter Text:')
	if reply == 'stop':
		break
	print(reply.upper())

# Another Loop.
while True:
	print('Type ctrl + C to stop')
# This is an infinite loop, usually to stop an infinite loop ctrl + c stops the loop.

while True:
	name = input ('Enter Name:')
	if name == "stop":
		break
	age = input ('Enter Age')
	print('Hello', name, '=>', int(age)**2)

# Here we have 2 user inputs, int(age) needs to be there because whatever the user inputs will be in the form of a string, so we need to convert into an integer before squaring.

# For loop example:
tot_sum = 0
for x in [1,2,3,4]:
	tot_sum = tot_sum + x
print(tot_sum)

# This adds all of the integers in the list

prod = 1
for item in [1,2,3,4]:
	prod *= item 
print(prod)

# Product of all the numbers within the list. here prod *= item is the same as prod = prod * item.

#=====================================================================

# Nesting For loops.
items = ["aaa", 111, (4,5), 2.01]		# set of objects
tests = [(4,5), 3.14]					# Keys to search for 

for key in tests:
	for item in  items:
		if item == key:					# check for match
			print(key, "was found")
			break
	else:
		print(key, "not found!")

# Another way to code this:

for key in tests:
	if key in items:					# We let python check for a match
		print(key, 'was found')
	else:
		print(key, 'not found!')

# Common items between 2 strings.

seq1 = "spam"
seq2 = "scam"

res =[]
for x in seq1:
	if x in seq2:
		res.append(x)

print(res)

# start an empty list res, scan first sequence, then the second sequence. 
# common item in both seq1 and seq2.