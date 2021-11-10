apples = input("Input the number of apples: ")

units = input("Weight in (k)kg or (l)lbs: ")

if units == "k":
    print(int(apples) / 5) 
else:
    print(int(apples) / 2.2)
