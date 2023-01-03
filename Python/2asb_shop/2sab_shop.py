import tkinter as tk
from tkinter import *
from tkinter import ttk


dict = {
	"size":["Large","Medium","Small"],
	"cost":[10,7,5],
}
list1 = []

dict_print = {
	"Size":[],
	"Quantity":[],
	"Bill":[], 
}

dict_bill = {
	"Total_Bill":[],
}

def buttonpress1():
	text_2.delete("1.0", "end-1c")
	price = 0
	input = int(text_1.get("1.0", "end-1c"))
	price = int(dict["cost"][dict["size"].index(n.get())]*input)
	dict_print["Size"].append(dict["size"][dict["size"].index(n.get())])
	dict_print["Quantity"].append(input)
	dict_print["Bill"].append(price)
	return price
	
def buttonpress2():
	text_2.delete("1.0", "end-1c")
	sum = 0
	price = 0
	price = buttonpress1()
	list1.append(price)
	for i in range(len(list1)):
		sum += list1[i]
	text_1.delete("1.0", "end-1c")
	return sum

def printprice():
	total_price = buttonpress2()
	if total_price!=0:
		text_2.insert(END, total_price," LE")
		dict_bill["Total_Bill"].append(total_price)
	else:
		price = buttonpress1()
		text_2.insert(END, price)
		dict_bill["Total_Bill"].append(price)
		
	#file = open("fatora.txt","x")
	file = open("fatora.txt","w+")

	file.write("\tFATORA")
	file.write("\n")
	file.write("*********************************")
	file.write("\n")
	length = len(dict_print["Size"])
	file.write("Size\tQuantity\tPrice")
	file.write("\n")
	for i in range(length):
		file.write(dict_print["Size"][i])
		file.write("\t")
		file.write(str(dict_print["Quantity"][i]))
		file.write("\t")
		file.write(str(dict_print["Bill"][i]))
		file.write(" LE")
		file.write("\n")
	file.write("*********************************")
	file.write("\n")
	file.write("Total Price:\t")
	file.write(str(dict_bill["Total_Bill"][0]))
	file.write(" LE")

	file.close()

	list1.clear()
		
window_1 = Tk()
window_1.title(" 2asb Shop ")
window_1.geometry('600x500')
 
b_g = PhotoImage(file = 'images.png')
b_g = b_g.subsample(1,1)
label_1 = Label(window_1,width=500,height=500, bg = "#BFBF3E")
label_1.place(x = 0,y = 0)
label_2 = Label(window_1, text = "Welcome to 2asb Shop",bg = "#BFBF3E",fg = "#FFFFD3", font = ('Verdana', 15)).pack(pady = 50)
label_3 = Label(window_1, text = "Menu: ",bg = "#BFBF3E",fg = "#FFFFD3" , font = ('Verdana', 12)).place(x = 50,y = 130 )
label_4 = Label(text="Large", bg="#BFBF3E", fg="black",font = ('Verdana', 10)).place(x=50,y = 160)
label_4 = Label(text="10", bg="#BFBF3E", fg="black",font = ('Verdana', 10)).place(x=120,y = 160)
label_4 = Label(text="Medium", bg="#BFBF3E", fg="black",font = ('Verdana', 10)).place(x=50,y = 180)
label_4 = Label(text="7", bg="#BFBF3E", fg="black",font = ('Verdana', 10)).place(x=120,y = 180)
label_4 = Label(text="Small", bg="#BFBF3E", fg="black",font = ('Verdana', 10)).place(x=50,y = 200)
label_4 = Label(text="5", bg="#BFBF3E", fg="black",font = ('Verdana', 10)).place(x=120,y = 200)

label_5 = Label(window_1, text = "Select Size: ",bg = "#BFBF3E",fg = "#FFFFD3" , font = ('Verdana', 12)).place(x = 50,y = 270 )
b1 = Button(window_1 , text = "Close" ,width= 7, bg="#FFFFD3" , fg = "black" , bd ='5', command = window_1.destroy).pack(side = BOTTOM)

label_6 = Label(window_1, image = b_g).place(x = 350,y = 130 )

n = tk.StringVar()
sizechoosen = ttk.Combobox(window_1, width = 27, textvariable = n, state='readonly')

sizechoosen['values'] = ('Large',
						  'Medium',
						  'Small')
						  
sizechoosen.place(x = 155, y = 270)
sizechoosen.current()

label_7 = Label(window_1, text = "Enter number of cups: ",bg = "#BFBF3E",fg = "#FFFFD3" , font = ('Verdana', 12)).place(x = 50,y = 350 )
text_1 = Text(window_1, width=7, height=2)
text_1.place(x=250 , y=348)

b2 = Button(window_1 , text = "Price" ,bg="#FFFFD3" , fg = "black" , width= 7, height= 1,bd ='5', command = printprice).place(x = 50, y = 400)
text_2 = Text(window_1, width=7, height=2)
text_2.place(x=140 , y=398)

b3 = Button(window_1 , text = "New order" ,bg="#FFFFD3" , fg = "black" , width= 7, height= 1,bd ='5', command = buttonpress2).place(x = 50, y = 450)

window_1.mainloop()


