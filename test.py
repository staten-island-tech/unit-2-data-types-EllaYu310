def gcf(a,b):
    if b==0:
        return a
    else:
        return gcf(b, a%b)
a = int(input("Enter a number:"))
b = int(input("Enter a numbter:"))

print(gcf(a,b))