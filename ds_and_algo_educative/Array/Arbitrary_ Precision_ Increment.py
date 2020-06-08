
##  Link for understanding
##    https: // www.youtube.com / watch?v = v6K3SfMv9WM & list = PL5tcWHG - UPH1YSW2RraQg2L2p5hQTIpNL & index = 2

'''print last element of array
   A=[1,2,3]
   print(A[-1])  '''

A1 = [1, 4, 9]
A2 = [9, 9, 9]

# s = ''.join(map(str, A))
# print(int(s) + 1)


def plus_one(A):
    A[-1] += 1    # add 1 to last element
    for i in reversed(range(1, len(A))):   # process from last element
        if A[i] != 10:   ## not a precesion case
            break
        A[i] = 0  # if 10 ,0 to current position and add 1(precesion) to next element
        A[i-1] += 1  # add 1
    if A[0] == 10:     ## in case [9,9,9], first element becomes 10
        A[0] = 1        # make 0th posn to 1 and append 0 to end
        A.append(0)    ## get [1,0,0,0]
    return A


print(plus_one(A1))
print(plus_one(A2))