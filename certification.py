size =  3 #int(input("fuf: "))
start_masive = [] #["1234", "1567", "-2", "computer science"]
finish_masive = []
i = 0

while i < size:
    start_masive.append(str(input()))
    i += 1

i = 0

while i < len(start_masive):
    if len(start_masive[i]) <= 3:
        finish_masive.append(start_masive[i])
    
    i += 1
print(finish_masive)
