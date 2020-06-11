
## watch video for understanding :
# https://www.youtube.com/watch?v=qjuXUWzVO_Q&list=PL5tcWHG-UPH03aqnBTkBuH5qIbhshbg_K&index=3

'''print(ord('A')- ord('A')+ 1)
print(ord('B')- ord('A')+ 1)
print(ord('C')- ord('A')+ 1)
print(ord('Z')- ord('A')+ 1)'''

def spreadsheet_encode_column(col_str):
    num = 0   # which we will return
    count = len(col_str)-1   ## count is as exponnant , e= (n-1)
    for s in col_str:    ## s is iterator
        num += 26**count * (ord(s) - ord('A') + 1) ## AB= A * 26^1 + B * 26^0) ,,,ord() used to get number form of A and B in this form
        count -= 1
    return num


print(spreadsheet_encode_column("ZZ"))