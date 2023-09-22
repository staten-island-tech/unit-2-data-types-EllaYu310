#Challenge tip calculator
bill=float(input("Enter bill amount:$"))
tip_percentage=int(input("Enter tip percentage:%"))
total_amount= (bill+((tip_percentage*bill)/100))
print(f"total_amount:{total_amount}")

#values = [1,2.23,5,7,2,30,15]
#print (values[3])

#x = "this is a thing"
#y= x.split( )
#z = y[0]
#print(y)
#print(z)

#challenge1
sentence= (input("Enter a sentence:"))
word_count= sentence.split()
print(word_count)

#Number_of_monkeys = input("How many monkeys are there?:")
#if Number_of_monkeys == "50": #if you use if you put the thing you want
    #print("correct")
#else: #else is used to show that you dont want it
    #print("incorrect")

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
def factors(number):
    factors=[]
    for i in range(number, number+i):
        if number/i ==0:
            return factors

number=input("Enter a number")
factanswer=int(input(factors))
print(f'Factors of {number} are {factors}')


##Challenge 2 arguments, find factor