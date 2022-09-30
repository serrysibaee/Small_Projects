import tkinter
from tkinter import ttk , StringVar
from tkinter import messagebox
import time
import turtle


# PDS program
# you can use the combo box for the answer 
font1 = ("Comic Sans MS",25)
font2 = ("tahoma",12)
font3 = ("Bauhaus 93 Regular",10)
font4 = ("Comic Sans MS",9)

win = tkinter.Tk()
lbls = ttk.Style()
lbls.configure("TLabel",font=font3,background="white")
win.title("learn test ")
#win.geometry("480x700+350+10")
win.resizable(True,False)
win.config(background="white")
#sv = StringVar()
#sv.set(0)
lbl = ttk.Label(win,text="welcome to the learn type test. PDS class ",font=font1,background="gray",foreground="blue").grid(row=1,column=0)
#lbl.config(font=font1,background="gray",foreground="white")
#lbl.pack()
lbl2 = ttk.Label(win,text="put a number from 1 to 3 in every text place after raeding the lines ",font=font2).grid(row=2,column=0)
#lbl2.pack()
lblHR = ttk.Label(win,text="______________________________________ ").grid(row=3,column=0)
#lblHR.pack()
Q1 = ttk.Label(win,text="1. I remember information better if i write it down or draw a picture of it.--------------------> ",font=font3).grid(row=4,column=0)
#Q1.pack()
bot = ttk.Entry(win,width=1,font="tahoma")
bot.grid(row=4,column=1)

#bot.config(width=2)
Q2 = ttk.Label(win,text="2.I remember thing better when i hear them instead of just reading or seeing them ------->.",font=font3).grid(row=5,column=0)
#Q2.pack()
bot2 = ttk.Entry(win,width=1,font="tohoma")
bot2.grid(row=5,column=1)
Q3 = ttk.Label(win,text="3. when i get something that has to be assembled , i just start doing it. i do not read the directions ----->",font=font3).grid(row=6,column=0)
bot3 = ttk.Entry(win,font="tahoma",width=1)
bot3.grid(row=6,column=1)
Q4 = ttk.Label(win,text="4.if i am taking a test i can see the page of the text or lecture notes where the answer is located ----->",font=font3).grid(row=7,column=0)
bot4 = ttk.Entry(win,font="tahoma",width=1)
bot4.grid(row=7,column=1)
Q5 = ttk.Label(win,text="5.i would rather the professor explain a graph chart or diagram than just show it to me .  ----->",font=font3).grid(row=8,column=0)
bot5 = ttk.Entry(win,font="tahoma",width=1)
bot5.grid(row=8,column=1)
Q6 = ttk.Label(win,text="6.when learning new things , i want to 'do it ' rather than hear about it  ----->",font=font3).grid(row=9,column=0)
bot6 = ttk.Entry(win,font="tahoma",width=1)
bot6.grid(row=9,column=1)
Q7 = ttk.Label(win,text="7. i would rather the instructor write the information on the board , use a PowerPoint , or show a biideo instead of just lecturing . ----->",font=font3).grid(row=10,column=0)
bot7 = ttk.Entry(win,font="tahoma",width=1)
bot7.grid(row=10,column=1)
Q8 = ttk.Label(win,text="8.I would rather listen to a book on tape than read it  . ----->",font=font3).grid(row=11,column=0)
bot8 = ttk.Entry(win,font="tahoma",width=1)
bot8.grid(row=11,column=1)
Q9 = ttk.Label(win,text="9.I enjoy making things, putting things together, and working with my hands. ----->",font=font3).grid(row=12,column=0)
bot9 = ttk.Entry(win,font="tahoma",width=1)
bot9.grid(row=12,column=1)
serry = bot9.get()
Q10 = ttk.Label(win,text="10.I am able to quickly conceptualize and visualize information. ----->",font=font3).grid(row=13,column=0)
bot10 = ttk.Entry(win,font="tahoma",width=1)
bot10.grid(row=13,column=1)
Q11 = ttk.Label(win,text="11.I learn best by hearing words. ----->",font=font3).grid(row=14,column=0)
bot11 = ttk.Entry(win,font="tahoma",width=1)
bot11.grid(row=14,column=1)
Q12 = ttk.Label(win,text="12.I have been called 'hyperactive' by my parents , spouse,partner,or proffesor. ----->",font=font3).grid(row=15,column=0)
bot12 = ttk.Entry(win,font="tahoma",width=1)
bot12.grid(row=15,column=1)
Q13 = ttk.Label(win,text="13. I have bo trouble reading maps , charts, and diagrams. ----->",font=font3).grid(row=16,column=0)
bot13 = ttk.Entry(win,font="tahoma",width=1)
bot13.grid(row=16,column=1)
Q14 = ttk.Label(win,text="14. I can usually pick up on small sounds like bells, crickets,and frogs, and distant sounds llike train whisteles. ----->",font=font3).grid(row=17,column=0)
bot14 = ttk.Entry(win,font="tahoma",width=1)
bot14.grid(row=17,column=1)
Q15 = ttk.Label(win,text="15.I use my hamds and gesture a lot when i speak to others . ----->",font=font3).grid(row=18,column=0)
bot15 = ttk.Entry(win,font="tahoma",width=1)
bot15.grid(row=18,column=1)
Qx = ttk.Label(win,text="--------------------------------------------------------------------------------------------------------------------------",font=font3).grid(row=19,column=0)

#botan = ttk.Button(win,text='the results',width=15)
#botan.grid(row=20,column=0)
#the answers 1, 4 , 7 , 10 , 13 visual - 2 , 5, 8 ,11 ,14 auditory - 3. 6 9 12 15 tictile
#Qx = ttk.Label(win,text="X. .--------------------> ",font=font3).grid(row=,column=)
alpha = []
def theadd ():
    
    #if bot.get() or bot2.get() or bot3.get()or bot4.get()or bot4.get()or bot5.get()or bot6.get()or bot7.get()or bot8.get()or bot9.get()or bot10.get()or bot11.get()or bot12.get()or bot13.get()or bot14.get()or bot15.get()  == "" :
     #   messagebox.showinfo("error","plaese start put nums in the empty feilds ")
    #if bot.get() or bot2.get() or bot3.get()or bot4.get()or bot4.get()or bot5.get()or bot6.get()or bot7.get()or bot8.get()or bot9.get()or bot10.get()or bot11.get()or bot12.get()or bot13.get()or bot14.get()or bot15.get()  == "q" :
     #   messagebox.showinfo("error","plaese start put nums in the empty feilds ")
    #if int(bot.get()) or int(bot2.get()) or int(bot3.get()) or int(bot4.get()) or int(bot5.get()) or int(bot6.get()) or int(bot7.get()) or int(bot8.get()) or int(bot9.get()) or int(bot10.get()) or int(bot11.get()) or int(bot12.get()) or int(bot13.get()) or int(bot14.get()) or int(bot15.get()) > 3  :
     #   messagebox.showinfo("more numbers","you have some fields has a number bigger than 3 ")
        
        
    visual = int(bot.get())+int(bot4.get())+int(bot7.get())+int(bot10.get())+int(bot13.get())
    audiotory = int(bot2.get())+int(bot5.get())+int(bot8.get())+int(bot11.get())+int(bot14.get())
    tactile = int(bot3.get())+int(bot6.get())+int(bot9.get())+int(bot12.get())+int(bot15.get())
    string = "your visual is "+" "+str(visual)+" your audiotory is "+" "+str(audiotory)+" "+"your tactile is "+" "+str(tactile)
    messagebox.showinfo("welocome",string)
botan = ttk.Button(win,text='the results',width=15,command=theadd)
botan.grid(row=20,column=0)



win.mainloop()




#all the qs then know witch to aud or ......