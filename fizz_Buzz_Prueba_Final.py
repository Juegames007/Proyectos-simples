listaxd = []
cero = 0
multiple_three = [] #[3,6,9,12,15]
multiple_five = [] # [5,10,15]
elevadothree = 1
elevadofive = 1

for _ in range(5):
    multiple_three.append(3*elevadothree)
    elevadothree = elevadothree + 1

for _ in range(3):
    multiple_five.append(5*elevadofive)
    elevadofive = elevadofive + 1

print(multiple_five)
print(multiple_three)

for _ in range(11):
    cero = cero + 1
    if cero in multiple_three and cero in multiple_five:
        listaxd.append("fizz_Buzz")
        cero = cero + 1
        listaxd.append(cero)
    elif cero in multiple_three: 
        listaxd.append("fizz")
        cero = cero + 1
        listaxd.append(cero)
    elif cero in multiple_five:
        listaxd.append("Buzz")
        cero = cero + 1
        listaxd.append(cero)
    else: 
        listaxd.append(cero)

#for _ in range(10):
    #for _ in range(2):
        #cero = cero + 1
        #listaxd.append(uno)
    #for _ in range(1):
        #listaxd.append("Fizz")
    #for _ in range(1):
        #cero = cero + 1

for i in listaxd:
    print(i)


        

        