

def bigger_guy(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(bigger_guy(100,50))

# bellow codee is optional
# this is designed to test your code.

def test_bigger_guy():
    assert bigger_guy(1, 2) == 2
    assert bigger_guy(10, 20) == 20
    assert bigger_guy(20, 10) == 20
    assert bigger_guy(10, 10) == 10
    assert bigger_guy(2, 1) == 2
    assert bigger_guy('a', 'b') == 'b'  # 'b' is greater than 'a'
    print("YOUR CODE IS CORRECT!")

test_bigger_guy()