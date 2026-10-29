def is_palindrome(text):
    text=text.replace(" ","").lower()
    return text == text[::-1]
print(is_palindrome("LEVel"))
print(is_palindrome("HeLLo"))
print(is_palindrome("racECar"))
print(is_palindrome("A man a PLAN a caNAl Panama"))
