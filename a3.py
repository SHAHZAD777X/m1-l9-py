n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

while n2!=0:
    t=n2
    n2=n1%n2
    n1=t

hcf=n1
print("HCF is:",hcf)
