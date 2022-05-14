print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = "Tim"
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name)


age = 24
print(age)

print(type(greeting)) #it prints the datatype of the vatriable
print(type(age))

age_in_words = "2 years"
# ERROR:

# print(name + " is " + age + "Years old")  Python knows what to do if you use + with two strings. It concatenates them,

#or with two numbers, it calculates their sum.

#However, it's got no idea what you intend if you try to add a string and a number.

#Some languages, such as Java, will automatically convert the number to a string and concatenate,

#but Python doesn't do this, hence the type error.

#this could be dealt with using f strings
# which is used for formatting
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
