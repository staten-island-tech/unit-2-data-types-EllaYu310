#Challenge tip calculator
bill=float(input("Enter bill amount:$"))
tip_percentage=int(input("Enter tip percentage:%"))
total_amount= (bill+((tip_percentage*bill)/100))
print(f"total_amount:{total_amount}")

#challenge1
sentence= (input("Enter a sentence:"))
word_count= sentence.split()
print (len(word_count))

##Challenge odd or even
number=7
if number%2 == 0: 
    print("Even")
else:
    print("Odd")
    
##Challenge bill
bill=(input("Enter bill amount:$"))
service=(input("What would you rate the service? bad, okay, good, or great?:"))
if service == "bad":
    print("0% tip?")
elif service == "okay":
    print("15% tip?")
elif service == "good":
    print("20% tip?")
elif service == "great":
    print("25% tip?")
else:
    print("Please rate our service.")
    
##Challenge Finding factors
factors=int(input("Enter a number:"))
for i in range(1, factors+1):
    if factors%i==0:
        print(i)

##Challenge Finding GCF
def GCF(a,b):
    for i in range(1, min(a,b)+1):
        if a%i==0 and b%i==0:
            GCF.append(i)
    return max(GCF)