n= int(input("Enter a number:"))
reverse = 0

temp = 0
while temp>0:
    remen = temp%10
    reverse = remen + (reverse*10)
    temp = int(temp/10)

if reverse==n:
    print("This is a palindrome number:")
else:
    print("Not a palndrome number:")