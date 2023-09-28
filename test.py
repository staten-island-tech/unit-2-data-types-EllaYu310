#Truth table
#x=9213
#y=True
#def truthy(x,y):
#    if type(x) !=bool or type(y) !=bool:
#        print("Error")
#    else:
#       if x==y:
#            print("False")
#        elif x!=y:
#            print("True")
#truthy(x,y)

#!=not equal

Eastbound_traffic=input("There is traffic on the Eastbound lane, True or False?:")
Westbound_traffic=input("There is traffic on the Westbound lane, True or False?:")
if Eastbound_traffic=="Truth" and Westbound_traffic=="True":
    print("Traffic on both sides.")
elif Eastbound_traffic=="Truth" and Westbound_traffic=="False":
    print("There is traffic on the east side.")
elif Eastbound_traffic=="False" and Westbound_traffic=="True":
    print("There is traffic on the west side.")
else:
    Print("Error")