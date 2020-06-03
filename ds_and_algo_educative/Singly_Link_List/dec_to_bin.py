

## convert decimal number into binary...return binary number as string


from stack import Stack   # stack.py

def convert_dec_to_bin(dec_num)  :

    s = Stack()      # obj of class Stack from stack.py

    while dec_num > 0 :
        remainder = dec_num % 2    ## conversion
        s.push(remainder)          ## push on stack
        dec_num = dec_num // 2     ## floor devesion

    bin_num = ""                    ## create empty string
    while not s.is_empty() :
        bin_num += str( s.pop())   ##  convert number to string
    return  bin_num                ## return binary number as a string

print(convert_dec_to_bin(56))
print(convert_dec_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))

print(int(convert_int_to_bin(56),2)==56)   # chack if conversion is corct or not
