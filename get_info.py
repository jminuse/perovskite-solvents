

f=open('gaussian/pbi2_1acetone_2.log').read() # this reads in whole file as a string
def find_charge(f, name): #this defines a function of the string created above and the term you want to search for
	return f.rfind(name) # this will return the term being searched for, from the string in reverese

print find_charge(f, "Mulliken charges:") # this returns the character number/position of the first letter of the term you searched for (top-down)



