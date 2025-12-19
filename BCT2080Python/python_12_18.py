import math ; print(math.sqrt(16))  #importing math module and using sqrt function to find square root of 16
import random; print(random.randint(1, 10))  #importing random module and using randint function to generate a random integer between 1 and 10
import datetime; now = datetime.datetime.now(); print(now)  #importing datetime module and getting the current date and time
import os; print(os.getcwd())  #importing os module and getting the current working directory
import json; data= {"name": "Alice", "age":30}; json_string = json.dumps(data);
print(json_string)  #importing json module and converting a dictionary to a JSON string

try:
    print(4 / 0)
except Exception as e:
    print(f"an error occured: {e}")  #handling division by zero error using try-except block

num=int(input("Enter an index to access in the list(0-2): "))
try:
    my_list = [1, 2, 3]
    print(my_list[num])
except Exception as e:
    print(f"an error occured: {e}")  #handling index out of range error using try-except block
else:
    print("No exception occurred")  #executed if no exception occurs
finally:
    print("Execution completed")  #always executed block

age = 16
try:
    if age < 18:
        raise ValueError("Age must be at least 18")  #raising a ValueError if age is less than 18
except ZeroDivisionError as e:
    print(f"an error occured: {e}")  #handling ZeroDivisionError
except ValueError as ve:
    print(f"Value error: {ve}")  #handling ValueError raised above
except Exception as ne:
    print(f"an error occured: {ne}")  #handling any other exceptions
else:
    print("No exception occurred")  #executed if no exception occurs
finally:
    print("Execution completed")  #always executed block


with open("sample.txt", "r") as file:
    data = file.read()  #this will give error as the file is opened in write mode
    print(data)


with open("sample.txt", "w") as file:
    file.write("Hello, World!")  #writing to a file using with statement
    file.write("\nWelcome to Python programming.")
    file.write("\nThis is a sample text file.")