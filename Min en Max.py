a = input("Geef een gehele getal ")
b = input("Geef een gehele getal ")

if a > b:
    Max = a
    Min = b
    print("a is het grootste getal: " + Max)
elif a < b:
    Max = b
    Min = a
    print("a is het kleinste getal: " + Min)
else:
    Max = a
    Min = a
    print("a en b zijn even groot")     
print("Het minimum is: " + Min)
print("Het maximum is: " + Max)