input = "dlrow nohtyp"
print(input[::-1]) #slicing to reverse the string ::-1 reverse the string
#str2.reverse() #this will give error as strings are immutable in python
#str2.[::-1] in this ::-1 indicates step value, meaning to take each character from the end to the start


def outer_function():
    outer_variable = "I am nonlocal"

    def inner_function():
        nonlocal outer_variable
        outer_variable = "I am modified"
        print(outer_variable)

    inner_function()
    print(outer_variable)

outer_function()

import keyword
print(keyword.kwlist)  #prints all the keywords in python
len(keyword.kwlist)  #prints the number of keywords in python
#count the keywords
count = 0
for kw in keyword.kwlist:
    count += 1
print(count)

# def my_function():
#     print("before continue")
#     continue
#     print("after continue")

# my_function() #this will give error as continue cannot be used outside loops 