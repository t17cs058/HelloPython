'''
Created on 2019/10/09

@author: t17cs058
'''
D = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
Nd = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }

n = ""

for x1 in D:
    for x2 in D:
        for x3 in D:
            for x4 in D:
                for x5 in D:
                    for x6 in D:
                        for x7 in D:
                            for x8 in Nd:
                                print(x1, x2, "(", x3, x4, x5, x6, x7, x8, ") =", "{ " + n + " }")
        if x2 == 0:
            n = "{ }"
        else:
            n += ", { " + n + " }"
