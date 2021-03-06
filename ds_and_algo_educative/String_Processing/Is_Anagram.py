
## https://www.youtube.com/watch?v=Pb7pmvifBf4&list=PL5tcWHG-UPH03aqnBTkBuH5qIbhshbg_K&index=4
######  Solution 1 #########

s1 = "fairy tales"
s2 = "rail safety"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

print (s1)
print(sorted(s1))
print(sorted(s2))


# Requires n log n time (since any comparison
# based sorting algorithm requires at least
# n log n time to sort).
print(sorted(s1) == sorted(s2))

######## Solution 2 #########

def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True

s1 = "fairy tales"
s2 = "rail safety"
## normalizing the strings
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

print(is_anagram(s1, s2))