# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

def rot13(message):
    result = []
    for i in message:
        if i.isalpha():
            if i.isupper():
                if ord(i)+13 > 90:
                    result.append(chr(ord(i)+13-26))
                else:
                     result.append(chr(ord(i)+13))
            else:
                if ord(i)+13 > 122:
                     result.append(chr(ord(i)+13-26))
                else:
                    result.append(chr(ord(i)+13))
        else:
            result.append(i)
    
    return "".join(result)