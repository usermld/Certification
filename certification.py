n =  3#int(input("fuf: "))
masive_1 = []
masive_2 = []
i = 0
minimal = "asd"

while i < n:
    masive_1 += [str(input())]
    i += 1
    
print(masive_1)

i = 0
for i in masive_1:
    if masive_1[i] < minimal:
        masive_2 += masive_1[i]
    i += 1

print(masive_1)
print(masive_2)