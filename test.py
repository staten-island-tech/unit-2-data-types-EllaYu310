##Challenge Finding GCF
#list=[]
#def greatest_common_factor(a,b):
#    for i in range(1, min(a,b)+1):
#        if a%i==0 and b%i==0:
#            list.append(i)
#number_1=int(input("Enter your first number:"))
#number_2=int(input("Enter your second number:"))
#print(max(list))

list=[]
def gcf(a,b):
    if number_1>number_2:
        smaller=number_2
    else:
        smaller=number_1
    for i in range(1, smaller+1):
        if number_1%i==0 and number_2%i==0:
            list.append(i)
number_1=int(input("Enter your first number:"))
number_2=int(input("Enter your second number:"))
gcf(number_1,number_2)
print(max(list))
