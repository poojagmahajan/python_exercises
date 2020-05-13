
## check for number is even

def is_even(number):
    if(number%2==0):
        #print("number is even")
        return True
    else:
        #print("Number is odd(Not even")
        return False

print(is_even(3))

#function to check that our code is correct or not
def test_is_even():
    assert is_even(2)==True
    assert is_even(50)==True
    assert is_even(25)==False
    print("Code is correct")

test_is_even()