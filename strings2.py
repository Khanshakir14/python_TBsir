#                   1
#         012345678901234
parrot = "Norwegian Blue"


#slicing
print(parrot[0:6])#it would slice the string upto 6 but not including six 6 #Norweg
print(parrot[0:9]) #it would print the first word
print(parrot[:9])
print(parrot[2:5])#rwe
print(parrot[10:15])
print(parrot[10:])
print()
print(parrot[:6] + parrot[6:])
#this is similar to
print(parrot[:])

#slicing with negative indexing
print(parrot[-14:-8]) #Norweg
print(parrot[-4:-2]) #Bl
print(parrot[-4:12]) #Bl

#lec30
#using a step in a slice

print(parrot[0:6:2])    # Nre #printing the slice from index 0 to 6 but not including 6 in a step of twos

print(parrot[0:6:3])    # Nw    #printing the slice from index 0 to 6 but not including 6 in a step of threes

number = "9,223;372:036 854,775;807"
seperators = number[1::4] #it is slicing in a step of 4
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
