def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Take input from the user
user_string = input("Enter a string: ")

# Check and display the result
if is_palindrome(user_string):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")


#OUTPUT
'''
Enter a string: CAR
The given string is not a palindrome
'''    
