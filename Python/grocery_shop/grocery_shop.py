import csv
import os
from prettytable import PrettyTable

Grocery_dict = {
    "List": ["Apple" , "Banana" , "Cherry"],
    "Stock":[10        , 15           , 20],
    "Price":[20        , 30           , 40],   
}

Customer_order = {
    "Bag":[],
    "Quantity":[],
    "Bill":[],

}

Customer_bill = {
    "Total_Bill":[],
}

state0 = True
state1 = True
state2 = True
print("          Welcome to ITI Shop\n")
while state0:
    print("For Customer     enter 1")
    print("For Shop Owner   enter 2")
    print("To exit          enter 0\n")
    ch=int(input("Please enter your choice: "))
    print()
    os.system('cls')
    if (ch == 0):
        print ("\n\t\t*** Thank you for using our Application ***")
        state0 = False
    #for customer   
    elif (ch == 1):
        while state1:
            print("Show our products  enter 1")
            print("Buy elements       enter 2")
            print("Print the Bill     enter 3")
            print("To exit            enter 0\n")
            ch_c=int(input("Please enter your choice: "))
            print()
            os.system('cls')
            ##if the input not in choices 
            if(ch_c == 0):
                print ("\n\t\t*** Thank you for using our Application ***")
                state1 = False
                state0 = False               
            elif(ch_c == 1):
                print(Grocery_dict["List"])
                print(Grocery_dict["Stock"])
                print(Grocery_dict["Price"])
                print()
            elif(ch_c == 2):
                element=input("Please enter the element you want to buy: ")
                while (element not in Grocery_dict["List"]):    #check if the element in the list
                    print("\nyour element is not in the list if you want to enter another element please enter yes")
                    reply = input("Enter your reply: ")
                    if(reply == "yes"):
                        element = input("Enter your element:  ")
                        print()
                    else:
                        print("\n\t\t*** Thank you for using our Application ***")
                        state1 = False
                        break
                        
                if(state1 == False): 
                    state0 = False    #exit the perogram
                else:
                    Customer_order["Bag"].append(Grocery_dict["List"][Grocery_dict["List"].index(element)])  #add the element chosen by customer to customer bag
                    quantity=int(input("Please enter the quantity that you need: "))
                    while(quantity > Grocery_dict["Stock"][Grocery_dict["List"].index(element)]): # check if the input quantity more than that in the stock
                        print("there is not enough for your order")
                        quantity = int(input("please enter another quantity: "))         
                    Customer_order["Quantity"].append(quantity)                 #add quantity entered by customer to customer quantity
                    Grocery_dict["Stock"][Grocery_dict["List"].index(element)] -= quantity  # subtract the quantity entered by customer from that in the stock
                    print(Customer_order["Bag"])
                    print(Customer_order["Quantity"])
                    print()         
            elif(ch_c == 3):
                bill = 0.0
                t_bill = 0.0 
                for i in range(len(Customer_order["Bag"])):
                    bill = Grocery_dict["Price"][Grocery_dict["List"].index(Customer_order["Bag"][i])] * Customer_order["Quantity"][i]    #calculate price
                    Customer_order["Bill"].append(bill)        #add the price of the things that customer took to customer bill
                    t_bill += bill #calculate total price
                Customer_bill["Total_Bill"].append(t_bill)  #add the total price of the things that customer took to customer bill
                myTable = PrettyTable(["Bag", "Quantity", "Bill"])
                for i in range(len(Customer_order["Bag"])):
                    myTable.add_row([Customer_order["Bag"][i],Customer_order["Quantity"][i],Customer_order["Bill"][i]])	
                myTable.add_row(["----","----","----"])
                myTable.add_row(["Total"," ",Customer_bill["Total_Bill"][0]])
                print(myTable)
                print()     
            else:
                print ("Your choice is invalid")
                state1 = False                                               
    elif (ch == 2):
        while state2:
            print("Show products     enter 1")
            print("Add new products  enter 2")
            print("Change cost       enter 3")
            print("To exit           enter 0\n")
            ch_o=int(input("Please enter your choice: "))
            print()
            os.system('cls')
            #if the input not in choices 
            if(ch_o == 0):
                print ("\n\t\t*** Thank you for using our Application ***")
                state2 = False
                state0 = False
            elif(ch_o == 1):
                print(Grocery_dict["List"])
                print(Grocery_dict["Stock"])
                print(Grocery_dict["Price"])
                print()
            elif(ch_o == 2):
                new_p = input("Please enter the element you want tot add: ")
                new_q = int(input("Enter it's quantity: "))
                new_c = int(input("Enter it's price: "))
                Grocery_dict["List"].append(new_p)
                Grocery_dict["Stock"].append(new_q)
                Grocery_dict["Price"].append(new_c)
                print(Grocery_dict["List"])
                print(Grocery_dict["Stock"])
                print(Grocery_dict["Price"])
            elif(ch_o == 3):
                print(Grocery_dict["List"])
                print(Grocery_dict["Stock"])
                print(Grocery_dict["Price"])
                product = input("Enter the product that you want to change it's price: ")
                new_price = int(input("Enter the new price: "))
                Grocery_dict["Price"][Grocery_dict["List"].index(product)] = new_price
                print(Grocery_dict["List"])
                print(Grocery_dict["Stock"])
                print(Grocery_dict["Price"])
                print()
            else:
                print ("Your choice is invalid")
                state2 = False    
    #if the input not in choices
    else:
        print ("Your choice is invalid ")

#file1 = open("ITI_shop.csv","x")
#file2 = open("ITI_fatora.csv","x")
file1 = open("ITI_shop.csv","w") 
file2 = open("ITI_fatora.csv","w") 

header1 = ['	','			ITI_Shop			']      

with open ('ITI_shop.csv','w',newline='') as csvf1:

    csvwriter = csv.DictWriter(csvf1, delimiter='\t', fieldnames = header1)
    csvwriter.writeheader()
    csvwriter = csv.writer(csvf1, dialect='excel')
    csvwriter.writerow(Grocery_dict.keys())
    csvwriter.writerows(zip(*Grocery_dict.values()))


csvf1.close()

header2 = ['	','			ITI_Fatora			']       
t_bill = 0.0
total_bill = ['Total_Bill','	=	',]
total_bill.append(Customer_bill["Total_Bill"][0])

with open ('ITI_fatora.csv','w',newline='') as csvf2:
    
    csvwriter = csv.DictWriter(csvf2, delimiter='\t', fieldnames = header2)
    csvwriter.writeheader()
    csvwriter = csv.writer(csvf2, dialect='excel')
    csvwriter.writerow(Customer_order.keys())
    csvwriter.writerows(zip(*Customer_order.values()))
    csvwriter.writerow(total_bill)

csvf2.close()   


#file4 = open("ITI_fatora_.txt","x")
file4 = open("ITI_fatora_.txt","w+")

file4.write("\tITI FATORA")
file4.write("\n")
file4.write("*********************************")
file4.write("\n")
length = len(Customer_order["Bag"])
file4.write("Product\tQuantity\tPrice")
file4.write("\n")
for i in range(length):
    file4.write(Customer_order["Bag"][i])
    file4.write("\t")
    file4.write(str(Customer_order["Quantity"][i]))
    file4.write("\t")
    file4.write(str(Customer_order["Bill"][i]))
    file4.write(" LE")
    file4.write("\n")
file4.write("*********************************")
file4.write("\n")
file4.write("Total Price:\t")
file4.write(str(Customer_bill["Total_Bill"][0]))
file4.write(" LE")

file4.close()




