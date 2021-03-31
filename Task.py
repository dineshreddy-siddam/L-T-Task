from itertools import permutations

s1 = "LEVEL"

def sub_string(s1):
    la = []
    for i in range(1,len(s1)+1):
        l1 = permutations(s1, i)
        for j in l1:
            sa = "".join(j)
            la.append(sa)
    print(la)
    print(len(la))
    return la


def palindrome_check(s1):
    l3 = []
    for i in s1:
        rev_str = i[::-1]
        if i == rev_str:
            l3.append(i)
    print("palindrome list is ", l3)
    print("palindrome count is ", len(l3))


l2 = sub_string(s1)
palindrome_check(list(set(l2)))

"""
......=*=......
....===*===....
..=====*=====..
=======*=======
..=====*=====..
....===*===....
......=*=......
"""


# input as number --> odd number
"""
..=*=..
===*===
..=*=..
"""


def pattern(x):
    v2 = x + x - 1
    c = 2
    len1 = x
    while len1:
        print(f"{'.' * int(v2/2)}{'=' * int(c/2)}*{'=' * int(c/2)}{'.' * int(v2/2)}")
        if int(len1) > int(x/2) + 1:
            v2 -= 4
            c += 4
        else:
            v2 += 4
            c -= 4
        len1 -= 1


pattern(7)