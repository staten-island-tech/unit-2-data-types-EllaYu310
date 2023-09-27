list=[]
def gcf(a,b):
    if number_1>number_2:
        small=number_2
    else:
        small=number_1
    for i in range(1, small+1):
        if number_1%i==0 and number_2%i==0:
            list.append(i)
gcf(number_1,number_2)
print(max(list))
            
number_1=int(input("Enter your first number:"))
number_2=int(input("Enter your second number:"))