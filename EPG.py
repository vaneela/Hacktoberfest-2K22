# a => 0,1
# b => 0-9
# c => 0,1,2,3
# d => 0-9
# e => 1,2
# f => 0,9
# g => 0,5,6,7,8,9
# h => 0-9
# i => 0-9
# j => 0-9
# k => 0-9
# l => 0-9
# m => 0-9

a=['0','1']
b=['0','1','2','3','4','5','6','7','8','9']
c=['0','1','2','3']
d=['0','1','2','3','4','5','6','7','8','9']
e=['1','2']
f=['0','1','2','3','4','5','6','7','8','9']
g=['0','5','6','7','8','9']
h=['0','1','2','3','4','5','6','7','8','9']
i=['0','1','2','3','4','5','6','7','8','9']
j=['0','1','2','3','4','5','6','7','8','9']
k=['0','1','2','3','4','5','6','7','8','9']
l=['0','1','2','3','4','5','6','7','8','9']
m=['0','1','2','3','4','5','6','7','8','9']

for A in a:
        for B in b:
            for C in c:
                for D in d:
                    for E in e:
                        for F in f:
                            for G in g:
                                for H in h:
                                    for I in i:
                                        for J in j:
                                            for K in k:
                                                for L in l:
                                                    for M in m:
                                                        z=A+B+C+D+E+F+G+H+I+J+K+L+M
                                                        print(z)

        



