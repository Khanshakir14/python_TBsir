#slice backwards
          #01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]#prints z to b backwards
print(backwards)
backwards = letters[25::-1]
print(backwards)
backwards = letters[::-1]   #it is a python idiom to reverse the sequence
print(backwards)

#while using negative indexing or more specifically while doing slicing in backwards
#remember the first index is greater than the second



#letters = ""

backwards = letters[::-1]
print(backwards)

# create a slice that produces the characters qpo
print(letters[16:13:-1])
print(letters[-10:-13:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])

#python idioms
print(letters[-4:])
print(letters[-1:])
print(letters[:1]) #useful for getting th first item in a sequence, without your code crashing
print(letters[0])
