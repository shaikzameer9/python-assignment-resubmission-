def isPalindrome(s): 
      
    # reverse to string print(s) 
    rev = ''.join(reversed(s)) 
  
    # Checking if both string are  
    # equal or not 
    if (s == rev): 
        return True
    return False
  
# main function 
s = input("enter a element :")
ans = isPalindrome(s) 
  
if (ans): 
    print("Yes") 
else: 
    print("No") 
