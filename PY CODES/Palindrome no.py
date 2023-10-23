num=input("Enter the Name or Number")
def pal(num):
    X=num[::-1]
    if X==num:
        print("palindrome")
    else:
        print("not a palindrome")

print(pal(num))