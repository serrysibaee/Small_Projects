import time

from pynput.keyboard import Controller,Key

# ==============functions==================
def test_number(x):
    if x <= 0:
        exit()
    else:
        return x


def typier():
    text = ''''''
    keyboard.type(text)
    

def sleeper(x):
    time.sleep(x)

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
def down():
    keyboard.press(Key.down)
    keyboard.release(Key.down)


def copier():
    # this functions press to copy the texts 
    with keyboard.pressed(Key.ctrl):
        keyboard.press('c')
        keyboard.release('c')

def paster():
    # this functions press to copy the texts 
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
      
def wind():
    # this for go from tab to other 
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

def new_tab():
    with keyboard.pressed(Key.ctrl):
        keyboard.press('t')
        keyboard.release('t')

def close_tab():
    with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.f4)
        keyboard.release(Key.f4)

def full_work():
   # sleeper(5) put this in the first of the program start
    sleeper(2)
    copier()
    sleeper(2)
    new_tab()
    sleeper(2)
    paster()
    sleeper(2)
    enter()
    sleeper(6) #wait for WU to open correctly
    typier()
    sleeper(2)
    enter()
    sleeper(2)
    #did not use it first to make sure it going well
    wind()
    sleeper(2)
    close_tab()
    sleeper(2)
    down()
    
    
    
    



#===============vars and objects============
keyboard = Controller()
#===========================================



#=========while loop work===================

'''
the program will ask the user how many time it will work
to copy and paste the massages in the accounts whatsup

'''

# print('''
# welcome to auto sender program to auto the whatsup massages sending
# process. please follow the instruction ''')
# time.sleep(1.5)
# print('''
# put the mouse on the first field you want to start with then click
# the program will start after five seconds from entering the number
# of feilds to do ''')
# time.sleep(1.5)
# print('''
# !!!!!!!!!!!!!!!!!!!!!!!! do not touch the keyboard or the mouse while
# the programs is working only for emmergency !!!!!!!!!!!!!!!!!!!!!!!
# ''')
# time.sleep(3)
# 
num_std = int(input("enter number of students to do "))
test_number(num_std)
# 
# print("number of students you entered is " , num_std)







time.sleep(5)
for i in range (0,num_std):
    full_work()