num=int(input("Enter the number:"))

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

res=factorial(num)
print("Factorial of the number:",res)
        
