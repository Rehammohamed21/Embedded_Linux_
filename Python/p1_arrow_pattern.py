import time
import os

def right_arrow(n):
    for r in range(0,n):                 #print vertical space before printing arrow
        print("\n")
    
    for r in range (0,n-1):
        for c in range(0,n*3-1):         #print horizontal space before printing arrow
            print("  ",end="")
        for c in range(0,n*2):           #print the upper part of arrow
            print("  ",end="")
        for c in range(0,r+1):			 #print the upper part of arrow
            print("* ",end="")
        print()
		
    for r in range (0,n*3-1):			 #print horizontal space before printing arrow
        print("  ",end="")
    for r in range (0,n*3):				 #print the middle part of arrow
        print("* ",end="")
    print()
	
    for r in range (0,n-1):
        for c in range(0,n*3-1):		 #print horizontal space before printing arrow
            print("  ",end="")
        for c in range(0,n*2):			 #print the lower part of arrow
            print("  ",end="")
        for c in range(0,n-r-1):		 #print the lower part of arrow
            print("* ",end="")
        print()

def upper_arrow(n):
    for r in range (0,n):
        for c in range(0,n*2-1):		 #print horizontal space before printing arrow
            print("  ",end="")
        for c in range(0,n-r):			 #print the upper part of arrow
            print("  ",end="")
        for c in range(0,2*r+1):		 #print the upper part of arrow
            print("* ",end="")
        print()
   
    for r in range (0,n*2):				 
        for c in range(0,n*2-1):		 #print horizontal space before printing arrow
            print("  ",end="") 
        for c in range(0,n):			 #print the lower part of arrow
            print("  ",end="")
        print("* ")
    print()

def left_arrow(n):
	for r in range(0,n):				 #print vertical space before printing arrow
		print("\n")
	
	for r in range (0,n-1):
		for c in range(0,n-r-1):		 #print the upper part of arrow
			print("  ",end="")
		for c in range(0,r+1):			 #print the upper part of arrow
			print("* ",end="")
		print()
		
	for r in range (0,n*3):				 #print the middle part of arrow
		print("* ",end="")
	print()
	
	for r in range (0,n-1):
		for c in range(0,r+1):			 #print the lower part of arrow
			print("  ",end="")
		for c in range(0,n-r-1):		 #print the lower part of arrow
			print("* ",end="")
		print()

def down_arrow(n):
	for r in range(0,n*3):				 #print vertical space before printing arrow
		print("\n")
	
	for r in range (0,n*2):
		for c in range(0,n*2):			 #print horizontal space before printing arrow
			print("  ",end="")
		for c in range(0,n-1):			 #print the upper part of arrow
			print("  ",end="")
		print("* ")
		
	for r in range (n,0,-1):
		for c in range(0,n*2):			 #print horizontal space before printing arrow
			print("  ",end="")
		for c in range(0,n-r):			 #print the lower part of arrow
			print("  ",end="")
		for c in range(0,2*r-1):		 #print the lower part of arrow
			print("* ",end="")
		print()

n = 6

no_loading= int(input("please enter number of itrations: "))

while no_loading:
    os.system('cls')
    no_loading-=1
    right_arrow(n)
    time.sleep(0.1)
    os.system('cls')
    upper_arrow(n)
    time.sleep(0.1)
    os.system('cls')
    left_arrow(n)
    time.sleep(0.1)
    os.system('cls')
    down_arrow(n)
    time.sleep(0.1)

    