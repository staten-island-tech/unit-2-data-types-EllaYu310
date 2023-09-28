#Eastbound_traffic=input("There is traffic on the Eastbound lane, True or False?:")
#Westbound_traffic=input("There is traffic on the Westbound lane, True or False?:")
#if Eastbound_traffic=="True" and Westbound_traffic=="False":
#    print("5 minutes of traffic in the eastbound lane.")
#elif Eastbound_traffic=="False" and Westbound_traffic=="True":
#    print("5 minutes of traffic in the Westbound lane.")
#else:
#    print("Error")

#Truth table
x=9213
y=True

def truthy(x,y):
    if type(x) !=bool or type(y) !=bool:
        print("Error")
    else:
        if x==y:
            print("False")
        elif x!=y:
            print("True")
truthy(x,y)