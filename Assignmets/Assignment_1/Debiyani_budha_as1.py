# Variables and String
my_age=19
print("my age is :",my_age)

fav_food=input("Enter your favourite food:")
print("Her favourite food is",fav_food)

#Type conversion
String="42"
integer=int(String)
print("string converted to integer:",integer)

float_value=3.14159
String_2=str(float_value)
print("float converted to string:",String_2)


#Strings
str1="Hello"
str2="World!"
print(str1+str2)

# Use string indexing to execute the third character from string "python"
str3="Python"
third_char=str3[2]
print("third character in :",str3,"is",third_char)

#Take a sentence as input and display the first five words
sentence = input("Enter a long sentence more than 5 words:")
"I am Debiyani and I am 19 years old"
"I" "am" "Debiyani" "and" "I" "am" "19" "years" "old"
print(sentence)
words=sentence.split()
five_words = " ".join(words[:5])
print(five_words)