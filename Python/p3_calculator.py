ch = True


while ch:
    print("For Arithmetic operations enter 1")
    print("For Logic operations      enter 2")
    print("For Programmer operations enter 3")
    print("For Exit                  enter 0\n")
    op_type = int(input("Please enter your choice: "))
    print()
    #choose arithmetic operations
    if op_type == 1:
        print("For Addition                   enter 1")
        print("For Subtraction               enter 2")
        print("For Multiplication operations  enter 3")
        print("For Division operations        enter 4")
        print("For reminder operations        enter 5")
        print("For Exponentiation operations  enter 6\n")
        ar_type=int(input("Please enter your choice: "))
        print()
		#if the input not in choices
        if ar_type < 1 or ar_type > 6:
            print("your choice is invalid")
            ch = False
        else:
            num1=int(input("please enter first number: "))
            num2=int(input("please enter second number: "))
            if ar_type == 1:
                print("\n",num1,"+",num2,"= %d\n"%(num1+num2))   
            elif ar_type == 2:
                print("\n",num1,"-",num2,"= %d\n"%(num1-num2))  
            elif ar_type == 3:
                print("\n",num1,"*",num2,"= %d\n"%(num1*num2))   
            elif ar_type == 4:
                while num2 == 0:           #checking the denominator if = 0
                    print("Math error can't divid by zero")
                    num1=int(input("please enter first number: "))
                    num2=int(input("please enter first number: "))
                print("\n",num1,"/",num2,"= %0.2f\n"%(num1/num2))      
            elif ar_type == 5:
                print("\n",num1,"%",num2,"= %d\n"%(num1%num2)) 
            else:
                print("\n",num1,"^",num2,"= %d\n"%(num1**num2))

	#choose logic operations
    elif op_type == 2:
        print("For AND                     enter 1")
        print("For OR                      enter 2")
        print("For XOR operations          enter 3")
        print("For NOT operations          enter 4")
        print("For Shift left operations   enter 5")
        print("For Shift right operations  enter 6\n")
        l_type=int(input("Please enter your choice: "))
        print()
		#if the input not in choices
        if l_type < 1 or l_type > 6:
            print("your choice is invalid")
            ch = False
        elif l_type == 4:
            num1=int(input("please enter number: "))
            print("\n~",num1,"= ",str(~num1),"\n")
        else:
            num1=int(input("please enter first number: "))
            num2=int(input("please enter second number: "))
            if l_type == 1:
                print("\n",num1,"&",num2,"= ",str(num1&num2),"\n")   
            elif l_type == 2:
                print("\n",num1,"|",num2,"= ",str(num1|num2),"\n")  
            elif l_type == 3:
                print("\n",num1,"^",num2,"= ",str(num1^num2),"\n")   
            elif l_type == 5:
                print("\n",num1,"<<",num2,"= ",str(num1<<num2),"\n") 
            else:
                print("\n",num1,">>",num2,"= ",str(num1>>num2),"\n")
    #choose programmer operations        
    elif op_type == 3:
        print("For conversion to decimal      enter 1")
        print("For conversion to binary       enter 2")
        print("For conversion to hexadecimal  enter 3")
        print("For conversion to octal        enter 4\n")
        pr_type=int(input("Please enter your choice: "))
        print()
		#if the input not in choices
        if pr_type < 1 or pr_type > 4:
            print("your choice is invalid")
            ch = False
        elif pr_type == 1:
            num=input("please enter number: ")
            num1=int(num,2)         #input nuber as binary number
            print("\nDecimal of number",num,"= %d\n"%(int(num1)))
        else:
            num=int(input("please enter number: "))
            if pr_type == 2:
                print("\nBinary of number",num,"=",str(bin(num)),"\n")   
            elif pr_type == 3:
                print("\nHexadecimal of number",num,"=",str(hex(num)),"\n")  
            else:
                print("\nOctal of number",num,"=",str(oct(num)),"\n")   
    #exit the program    
    elif op_type == 0:
        print("End Program")
        ch = False
    #if the input not in choices   
    else:
        print("your choice is invalid")
        
