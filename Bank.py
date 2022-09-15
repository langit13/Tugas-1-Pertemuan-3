
sapaan=input("").lower().strip()
x=sapaan.split(',')

if sapaan=="hello":
    uang=0
elif (x[0]=="hello"):
    uang=0
elif sapaan[0]=="h":
    uang=20
else:
    uang=100

print('$', uang)
