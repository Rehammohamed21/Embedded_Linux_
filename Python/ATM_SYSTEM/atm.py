from tkinter import*
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
import time 
import pyttsx3			

img_name = 'img.jpg'
WIDTH, HEIGHT = 820, 820

engine = pyttsx3.init()
voices = engine.getProperty("voices")		
rate = engine.getProperty("rate")

def speak1():
    mytext = "Your password is wrong, please try again"		
    engine.setProperty("rate", 150)				#rate of the speaking speed
    engine.setProperty("voice", voices[1].id)	#select the voice that you want from voices that is in the engine
    engine.say(mytext)
    engine.runAndWait()

def speak2():
    mytext = "Thank you for using our system"		
    engine.setProperty("rate", 150)				#rate of the speaking speed
    engine.setProperty("voice", voices[1].id)	#select the voice that you want from voices that is in the engine
    engine.say(mytext)
    engine.runAndWait()

def check_password():
    if my_password.get() == '1234':				#check if the password like that we determined
       my_password.set('')
       #wrong_pass_label['text']=''				#if password right no message will appear 
       show_frame(MenuPage)						#move to menu page
    else:
        #wrong_pass_label['text']='Incorrect Password !'		#if password wrong, a warning message will appear 
        speak1()													#voice with warning message will speak 
        my_password.set('')
                   
                  
def enter_dep():
    global current_balance
    global amount_dep_res
    amount_dep_res += int(amount_dep.get())				#The sum of the amount entered if the user entered an amount of money more than once
    current_balance += int(amount_dep.get())			#add the amount entered by user to the balance
    label4['text']= current_balance						#show new amount in the balance page
    status = tk.messagebox.askyesno("completion","Do you want to perform another operation?")
    if status == True:
        show_frame(MenuPage)
        amount_dep.set('')
    else:
        exit()

def enter_with():
    global current_balance
    global amount_with_res
    amount_with_res += int(amount_with.get())
    current_balance -= int(amount_with.get())			#reduce the amount entered by user to the balance
    label4['text']= current_balance
    status = tk.messagebox.askyesno("completion","Do you want to perform another operation?")
    if status == True:
        show_frame(MenuPage)
        amount_with.set('')
    else:
        exit()

def enter_with_100():
    global current_balance
    global amount_with_res
    amount_with.set('100')
    amount_with_res += int(amount_with.get())
    current_balance -= int(amount_with.get())
    label4['text']= current_balance
    status = tk.messagebox.askyesno("completion","Do you want to perform another operation?")
    if status == True:
        show_frame(MenuPage)
        amount_with.set('')
    else:
        exit()
   
    
def enter_with_200():
    global current_balance
    global amount_with_res
    amount_with.set('200')
    amount_with_res += int(amount_with.get())
    current_balance -= int(amount_with.get())
    label4['text']= current_balance
    status = tk.messagebox.askyesno("completion","Do you want to perform another operation?")
    if status == True:
        show_frame(MenuPage)
        amount_with.set('')
    else:
        exit()
    

def enter_with_300():
    global current_balance
    global amount_with_res
    amount_with.set('300')
    amount_with_res += int(amount_with.get())
    current_balance -= int(amount_with.get())
    label4['text']= current_balance
    status = tk.messagebox.askyesno("completion","Do you want to perform another operation?")
    if status == True:
        show_frame(MenuPage)
        amount_with.set('')
    else:
        exit()
    
    
def enter_with_1000():
    global current_balance
    global amount_with_res
    amount_with.set('1000')
    amount_with_res += int(amount_with.get())
    current_balance -= int(amount_with.get())
    label4['text']= current_balance
    status = tk.messagebox.askyesno("completion","Do you want to perform another operation?")
    if status == True:
        show_frame(MenuPage)
        amount_with.set('')
    else:
        exit()
    

def enter_with_2000():
    global current_balance
    global amount_with_res
    amount_with.set('2000')
    amount_with_res += int(amount_with.get())
    current_balance -= int(amount_with.get())
    label4['text']= current_balance
    status = tk.messagebox.askyesno("completion","Do you want to perform another operation?")
    if status == True:
        show_frame(MenuPage)
        amount_with.set('')
    else:
        exit()


def enter_with_3000():
    global current_balance
    global amount_with_res
    amount_with.set('3000')
    amount_with_res += int(amount_with.get())
    current_balance -= int(amount_with.get())
    label4['text']= current_balance
    status = tk.messagebox.askyesno("completion","Do you want to perform another operation?")
    if status == True:
        show_frame(MenuPage)
        amount_with.set('')
    else:
        exit()
    
def tick():
    current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')			#show time in hours,minutes and am or pm
    time_label.config(text=current_time)
    time_label.after(200,tick)
  
    
def exit():
    exit= tkinter.messagebox.askyesno("ATM","Do You Want to Print Receipt?")
    if exit == True:
        speak2()
        print("\tReceipt")
        print("******************************\n")
        if amount_dep_res != 0:
            print("Your Balance Was: 10000")
            print("Deposit Amount  :",amount_dep_res)
            print("Your Balance Now:",current_balance)
        elif amount_with_res != 0:
            print("Your Balance Was: 10000")
            print("Withdraw Amount :",amount_with_res)
            print("Your Balance Now:",current_balance)
        elif (amount_with_res != 0) and (amount_dep_res != 0):
            print("Your Balance Was: 10000")
            print("Deposit Amount  :",amount_dep_res)
            print("Withdraw Amount :",amount_with_res)
            print("Your Balance Now:",current_balance)
        else:
            print("Your Balance : 10000")
        print("\n******************************")
        window.destroy()
    else:
        speak2()
        window.destroy()
    return
       

window = tk.Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.title("ATM SYSTEM")
window.state('zoomed')			#make the window fill the full screen

current_balance = 10000
amount_with = tk.StringVar()
amount_with.set('')
amount_dep = tk.StringVar()
amount_dep.set('')
amount_dep_res = 0
amount_with_res = 0

#desired pages of the application
StartPage = tk.Frame(window)
MenuPage = tk.Frame(window)
WithdrawPage = tk.Frame(window)
AmountPage = tk.Frame(window)
DepositPage = tk.Frame(window)
BalancePage = tk.Frame(window)

frames = {}
for fr in (StartPage, MenuPage, WithdrawPage,AmountPage , DepositPage, BalancePage):
    fr.grid(row=0, column=0, sticky='nsew')
    
def show_frame(frame):
    frame.tkraise()			#make the frame appearing

show_frame(StartPage)

# ----------------   Start page  ----------------

img = ImageTk.PhotoImage(Image.open(img_name).resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS))
lbl = tk.Label(StartPage, image=img)
lbl.photo = img  # Keep a reference in case this code put is in a function.
lbl.place(relx=0, rely=0, anchor='nw')  

StartPage.configure(bg='#48483D')
label = tk.Label(StartPage, text='Welcome To Our System ', font=('calibre', 30, 'bold'), bg='#48483D', fg='white')
label.place(x=950, y=50)

Pass_label = tk.Label(StartPage, text='Enter Your Password', font=('calibre', 20, 'bold'), bg='#48483D', fg='white')
Pass_label.place(x=900, y=350)

my_password = tk.StringVar()

pass_entry = tk.Entry(StartPage, textvariable=my_password, font =('calibre',15,'normal'), show = '*', bd=5)
pass_entry.place(x=1220, y=350)
pass_entry.place(width=200, height=40)

log_button = Button(StartPage, text='Submit', font=('calibre', 15, 'bold'),width=10,height=2, fg='#48483D', relief='raised',command=check_password)
log_button.place(x=1100, y=450)

#wrong_pass_label = tk.Label(StartPage, text='',font=('calibre',15, 'bold'),fg='white', bg='#48483D', anchor='n')
#wrong_pass_label.place(x=910, y=480)

bottom_frame = tk.Frame(StartPage,relief='raised',borderwidth=3)
bottom_frame.pack(fill='x',side='bottom')

visa_photo = tk.PhotoImage(file='visa.png')
visa_label = tk.Label(bottom_frame,image=visa_photo)
visa_label.pack(side='left')
visa_label.image = visa_photo

mastercard_photo = tk.PhotoImage(file='mastercard.png')
mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
mastercard_label.pack(side='left')
mastercard_label.image = mastercard_photo

american_express_photo = tk.PhotoImage(file='american-express.png')
american_express_label = tk.Label(bottom_frame,image=american_express_photo)
american_express_label.pack(side='left')
american_express_label.image = american_express_photo

time_label = tk.Label(bottom_frame,font=('orbitron',12),fg='#48483D')
time_label.pack(side='right')

tick()

# ----------------   Menu page   ----------------

MenuPage.configure(bg='#48483D')
label1 = tk.Label(MenuPage, text='Main Menu', font=('calibre', 40, 'bold'), bg='#48483D', fg='white')
label1.place(x=635, y=50)

withdraw_button= Button(MenuPage, text='Withdraw', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised', command=lambda: show_frame(WithdrawPage)).place(x=650 , y=200)
deposit_button= Button(MenuPage, text='Deposit', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=lambda: show_frame(DepositPage)).place(x=650 , y=300)
bal_button= Button(MenuPage, text='Balance', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=lambda: show_frame(BalancePage)).place(x=650 , y=400)
exit_button= Button(MenuPage, text='Exit', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised', command=exit).place(x=650 , y=500)

bottom_frame = tk.Frame(MenuPage,relief='raised',borderwidth=3)
bottom_frame.pack(fill='x',side='bottom')

visa_photo = tk.PhotoImage(file='visa.png')
visa_label = tk.Label(bottom_frame,image=visa_photo)
visa_label.pack(side='left')
visa_label.image = visa_photo

mastercard_photo = tk.PhotoImage(file='mastercard.png')
mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
mastercard_label.pack(side='left')
mastercard_label.image = mastercard_photo

american_express_photo = tk.PhotoImage(file='american-express.png')
american_express_label = tk.Label(bottom_frame,image=american_express_photo)
american_express_label.pack(side='left')
american_express_label.image = american_express_photo

time_label = tk.Label(bottom_frame,font=('orbitron',12),fg='#48483D')
time_label.pack(side='right')

tick()

# ---------------- Withdraw page ----------------
WithdrawPage.configure(bg='#48483D')

label6 = tk.Label(WithdrawPage, text='Withdraw Window', font=('calibre', 40, 'bold'), bg='#48483D', fg='white')
label6.place(x=550, y=50)

button_100 = Button(WithdrawPage, text='100', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=enter_with_100)
button_100.place(x=10, y=250)

button_200 = Button(WithdrawPage, text='200', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=enter_with_200)
button_200.place(x=10, y=350)

button_300 = Button(WithdrawPage, text='300', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=enter_with_300)
button_300.place(x=10, y=450)

button_other = Button(WithdrawPage, text='Other', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=lambda: show_frame(AmountPage))
button_other.place(x=10, y=550)

button_1000 = Button(WithdrawPage, text='1000', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=enter_with_1000)
button_1000.place(x=1275, y=250)

button_2000 = Button(WithdrawPage, text='2000', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=enter_with_2000)
button_2000.place(x=1275, y=350)

button_3000 = Button(WithdrawPage, text='3000', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=enter_with_3000)
button_3000.place(x=1275, y=450)

menu_button3= Button(WithdrawPage, text='Return Menu', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=lambda: show_frame(MenuPage)).place(x=1275, y=550)

bottom_frame = tk.Frame(WithdrawPage,relief='raised',borderwidth=3)
bottom_frame.pack(fill='x',side='bottom')

visa_photo = tk.PhotoImage(file='visa.png')
visa_label = tk.Label(bottom_frame,image=visa_photo)
visa_label.pack(side='left')
visa_label.image = visa_photo

mastercard_photo = tk.PhotoImage(file='mastercard.png')
mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
mastercard_label.pack(side='left')
mastercard_label.image = mastercard_photo

american_express_photo = tk.PhotoImage(file='american-express.png')
american_express_label = tk.Label(bottom_frame,image=american_express_photo)
american_express_label.pack(side='left')
american_express_label.image = american_express_photo

time_label = tk.Label(bottom_frame,font=('orbitron',12),fg='#48483D')
time_label.pack(side='right')

tick()

# ---------------- Amount page  ----------------
AmountPage.configure(bg='#48483D')

label7 = tk.Label(AmountPage, text='Withdraw Window', font=('calibre', 40, 'bold'), bg='#48483D', fg='white')
label7.place(x=550, y=50)

amount_label1 = tk.Label(AmountPage, text='Enter The Amount', font=('calibre',30, 'bold'), bg='#48483D', fg='white')
amount_label1.place(x=470, y=240)

amount_entry1 = tk.Entry(AmountPage, textvariable=amount_with, font =('calibre',15,'normal'), bd=5)
amount_entry1.place(x=870, y=250)
amount_entry1.place(width=200, height=40)

enter_button1 = Button(AmountPage, text='Enter', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=enter_with)
enter_button1.place(x=650, y=400)

menu_button2= Button(AmountPage, text='Return Menu', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=lambda: show_frame(MenuPage)).place(x=650 , y=550)

bottom_frame = tk.Frame(AmountPage,relief='raised',borderwidth=3)
bottom_frame.pack(fill='x',side='bottom')

visa_photo = tk.PhotoImage(file='visa.png')
visa_label = tk.Label(bottom_frame,image=visa_photo)
visa_label.pack(side='left')
visa_label.image = visa_photo

mastercard_photo = tk.PhotoImage(file='mastercard.png')
mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
mastercard_label.pack(side='left')
mastercard_label.image = mastercard_photo

american_express_photo = tk.PhotoImage(file='american-express.png')
american_express_label = tk.Label(bottom_frame,image=american_express_photo)
american_express_label.pack(side='left')
american_express_label.image = american_express_photo

time_label = tk.Label(bottom_frame,font=('orbitron',12),fg='#48483D')
time_label.pack(side='right')

tick()

# ---------------- Deposit page  ----------------
DepositPage.configure(bg='#48483D')

label5 = tk.Label(DepositPage, text='Deposit Window', font=('calibre', 40, 'bold'), bg='#48483D', fg='white')
label5.place(x=550, y=50)

amount_label = tk.Label(DepositPage, text='Enter The Amount', font=('calibre',30, 'bold'), bg='#48483D', fg='white')
amount_label.place(x=470, y=240)


amount_entry = tk.Entry(DepositPage, textvariable=amount_dep, font =('calibre',15,'normal'), bd=5)
amount_entry.place(x=870, y=250)
amount_entry.place(width=200, height=40)

enter_button = Button(DepositPage, text='Enter', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=enter_dep)
enter_button.place(x=650, y=400)

menu_button1= Button(DepositPage, text='Return Menu', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=lambda: show_frame(MenuPage)).place(x=650 , y=550)

bottom_frame = tk.Frame(DepositPage,relief='raised',borderwidth=3)
bottom_frame.pack(fill='x',side='bottom')

visa_photo = tk.PhotoImage(file='visa.png')
visa_label = tk.Label(bottom_frame,image=visa_photo)
visa_label.pack(side='left')
visa_label.image = visa_photo

mastercard_photo = tk.PhotoImage(file='mastercard.png')
mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
mastercard_label.pack(side='left')
mastercard_label.image = mastercard_photo

american_express_photo = tk.PhotoImage(file='american-express.png')
american_express_label = tk.Label(bottom_frame,image=american_express_photo)
american_express_label.pack(side='left')
american_express_label.image = american_express_photo

time_label = tk.Label(bottom_frame,font=('orbitron',12),fg='#48483D')
time_label.pack(side='right')

tick()

# ---------------- Balance page  ----------------
BalancePage.configure(bg='#48483D')

label2 = tk.Label(BalancePage, text='Balance Window', font=('calibre', 40, 'bold'), bg='#48483D', fg='white')
label2.place(x=550, y=50)

label3 = tk.Label(BalancePage, text="Balance : ", font=('calibre', 30, 'bold'), bg='#48483D', fg='white')
label3.place(x=620, y=250)
label4 = tk.Label(BalancePage, text=current_balance, font=('calibre', 30, 'bold'), bg='#48483D', fg='white')
label4.place(x=820, y=250)


menu_button= Button(BalancePage, text='Return Menu', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised',command=lambda: show_frame(MenuPage)).place(x=650 , y=400)
exit_button= Button(BalancePage, text='Exit', font=('calibre', 15, 'bold'),width=20,height=3, fg='#48483D', relief='raised', command=exit).place(x=650 , y=500)

bottom_frame = tk.Frame(BalancePage,relief='raised',borderwidth=3)
bottom_frame.pack(fill='x',side='bottom')

visa_photo = tk.PhotoImage(file='visa.png')
visa_label = tk.Label(bottom_frame,image=visa_photo)
visa_label.pack(side='left')
visa_label.image = visa_photo

mastercard_photo = tk.PhotoImage(file='mastercard.png')
mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
mastercard_label.pack(side='left')
mastercard_label.image = mastercard_photo

american_express_photo = tk.PhotoImage(file='american-express.png')
american_express_label = tk.Label(bottom_frame,image=american_express_photo)
american_express_label.pack(side='left')
american_express_label.image = american_express_photo

time_label = tk.Label(bottom_frame,font=('orbitron',12),fg='#48483D')
time_label.pack(side='right')

tick()

window.mainloop()
