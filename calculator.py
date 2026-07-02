a=int(input("Enter a:"))
b=int(input("Enter b:"))
mode=int(input("Enter mode:"))
print ("Select 1 for add 2 for sub 3 for mul 4 for div 5 for mod")
match mode:
    case 1:
        Res=a+b
    case 2:
        Res=a-b
    case 3:
        Res=a*b
    case 4:
        Res=a/b
    case 5:
        Res=a%b

print("Res:",Res)
