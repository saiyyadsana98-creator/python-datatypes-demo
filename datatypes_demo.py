#  Declare variables of different data types
int_var = 25                 # Integer type
float_var = 4.5              # Float type
string_var = "Python"        # String type
bool_var = True              # Boolean value 

#  Print the type of each variable
print("int_var:", int_var, "| Type:", type(int_var))
print("float_var:", float_var, "| Type:", type(float_var))
print("string_var:", string_var, "| Type:", type(string_var))
print("bool_var:", bool_var, "| Type:", type(bool_var))

# Perform arithmetic operations
print("Addition:", int_var + float_var)
print("Subtraction:", int_var - float_var)
print("Multiplication:", int_var * float_var)
print("Division:", int_var / float_var)

# Convert string input to integer and float
try:
    user_input = input("Enter a number: ")
    
    int_value = int(user_input)      
    print("Integer value:", int_value)
    
    float_value = float(user_input) 
    print("Float value:", float_value)

except ValueError:
    # Handle invalid input
    print("Error: Please enter a valid numeric value.")

#  Proper concatenation of string and number
age = 20
message = "My age is " + str(age) 
print(message)

#  Dynamic typing example
data = 100
print("Value:", data, "| Type:", type(data))

data = "Now I am a string"
print("Value:", data, "| Type:", type(data))

data = 10.75
print("Value:", data, "| Type:", type(data))