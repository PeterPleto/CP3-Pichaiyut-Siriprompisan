number = int(input("Select your number: "))
k=number-1
j=1
for i in range(number):
    print(" "*k,j*"*")
    k-=1
    j+=2