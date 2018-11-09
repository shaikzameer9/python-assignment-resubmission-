anystring=input("Enter the string to be converted uppercase: ")

for i in range (0,len(anystring)):

   x=ord(anystring[i])
   if x>=97 and x<=122:
       x=x-32
   y=chr(x)
   print(y,end="")