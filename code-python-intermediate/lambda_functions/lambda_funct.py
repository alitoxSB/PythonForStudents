#function for palindrome detection
def palindrome(msj):
    if (msj == msj[::-1]):
        return True
    else:
        return False

#now with lambda functions
palindrome_lambda = lambda string: string == string[::-1]

if __name__== '__main__':
    print("normal function: ", palindrome("asa"))
    print("Lambda function: ", palindrome_lambda("asa"))
    
    