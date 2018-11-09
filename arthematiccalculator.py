# function to add two number
def add(x,y):
	return x+y
# function to subtract
def subtract(x,y):
	return x-y
# function to multiply
def multiply(x,y):
	return x*y
# function to divivde
def divivde(x,y):
	return x/y
print("select operation -\n" \
	"1. add \n" \
	"2. subtract \n" \
	"3. multiply \n" \
	"4. divivde \n")
# take input from the user  
select = input("Select operations form 1, 2, 3, 4 :") 
  
x = int(input("Enter any number: ")) 
y = int(input("Enter any number: ")) 
if select == '1': 
    print(x, "+", y, "=", 
                    add(x, y)) 
  
elif select == '2': 
    print(x, "-", y, "=", 
                    subtract(x, y)) 
  
elif select == '3': 
    print(x, "*", y, "=", 
                    multiply(x, y)) 
  
elif select == '4': 
    print(x, "/", y, "=", 
                    divide(x, y)) 
else: 
    print("Invalid input") 
