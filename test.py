Eastbound_traffic=input("There is traffic on the Eastbound lane, True or False?:")
Westbound_traffic=input("There is traffic on the Westbound lane, True or False?:")
if Eastbound_traffic=="True" and Westbound_traffic=="False":
    print("5 minutes of traffic in the eastbound lane.")
elif Eastbound_traffic=="False" and Westbound_traffic=="True":
    print("5 minutes of traffic in the Westbound lane.")
else:
    print("Error")

Eastbound_traffic=input("There is traffic on the Eastbound lane, True or False?:")
Westbound_traffic=input("There is traffic on the Westbound lane, True or False?:")

if not Eastbound_traffic=="True" and Westbound_traffic=="True":
    print("False")

elif not Eastbound_traffic=="False" and Westbound_traffic=="True":
    print("True")

elif not Eastbound_traffic=="True" and Westbound_traffic=="False":
    print("True")

elif not Eastbound_traffic=="False" and Westbound_traffic=="False":
    print("True")