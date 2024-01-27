n =  3 #int(input("fuf: "))
masive_1 = [] #["1234", "1567", "-2", "computer science"]
masive_2 = []
i = 0

while i < n:
    masive_1.append(str(input()))
    i += 1

i = 0

while i < len(masive_1):
    if len(masive_1[i]) <= 3:
        masive_2.append(masive_1[i])
    
    i += 1
print(masive_2)
