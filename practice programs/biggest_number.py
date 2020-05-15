

### def biggest_guy(num1,num2,num3):
##    numbers=[num1,num2,num3]
##    numbers.sort()
##    return numbers[-1]

def biggest_guy(num1,num2,num3):
    #bigger_guy = 0
    if num1 > num2 :
        bigger_guy = num1
    else:
        bigger_guy = num2

    if bigger_guy > num3 :
        biggest_guy = bigger_guy
    else :
        biggest_guy = num3

    return biggest_guy

print(biggest_guy(100,50,2))
_guy()
