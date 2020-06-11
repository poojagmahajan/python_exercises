
##  https://www.youtube.com/watch?v=qjuXUWzVO_Q&list=PL5tcWHG-UPH03aqnBTkBuH5qIbhshbg_K&index=3


'''s = "Was it a cat I saw?"

# Solution uses extra space proportional to size of string "s"
s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
this removes all speces,capital letters,numerics,punctuations

print(s == s[::-1])'''


def is_palindrome(s):
    i = 0  # start
    j = len(s) - 1   # End

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

s = "Was it a cat I saw?"
print(is_palindrome(s))