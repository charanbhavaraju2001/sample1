#this program checks if the entered string is a pangram or not
#a pangram is a sentence which contains every alphabet of the english language


def checkpangram(s):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabets :
        #I used .upper() to avoid any errors with capital or small letters
        if i.upper() in s.upper() :
            
            continue
        
        else :
            
            return ("The given string is not a pangram")

        
        #if the for loop is completed then we return the message
    return("The given string is a pangram")



s = input("Enter the string")

result = checkpangram(s)

print(result)
