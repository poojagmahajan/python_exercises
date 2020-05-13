

str = "Pooja"

#str_len = len(str)
#print(str_len)


##using function

def string_length(string):
    count = 0
    for letter in string:
        count += 1

    return count
def test_string_length():
    assert string_length('hello!') == 6
    assert string_length('banana') == 6
    assert string_length('8') == 1
    assert string_length('funnyguys') == 9
    assert string_length('101') == 3
    print("YOUR CODE IS CORRECT!")

test_string_length()