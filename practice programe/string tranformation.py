


#Given a getStr() function, write the necessary sequence of operations to transform the string
#(containing three literals) in such a way that every literal is tripled​ respectively.

#Sample Input =  abc

#Sample Output =  aaabbbccc

def getStr(s):
    s = (s[0]*3) + (s[1] * 3) + (s[2] * 3)

    strlen = len(s)

    #print(s,strlen)
    return(s,strlen)

#getStr("abc")
print(getStr("abc"))
