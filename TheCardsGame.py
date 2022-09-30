import time 

##
##Card1 = [1 ,11 ,21 ,31 ,41 ,51 ,3 ,13 ,23 ,33 ,43 ,53 ,5 ,15 ,25 ,35 ,45 ,55 ,7 ,17 ,27 ,37 ,47 ,57 ,9 ,19 ,29 ,39 ,49 ,59]
##Card2 = [32,37,42,47,52,57,33,38,43,48,53,58,34,39,44,49,54,59,35,40,45,50,55,60,36,41,46,51,56]
##Card3 = [2,11,22,31,42,51,3,14,23,34,43,54,6,15,26,35,46,55,7,18,27,38,47,58,10,19,30,39,50,59]
##Card4 = [8,13,26,31,44,57,9,14,27,40,45,58,10,15,28,41,46,59,11,24,29,42,47,60,12,25,30,43,56]
##Card5 = [4,13,22,31,44,53,5,14,23,36,45,54,6,15,28,37,46,55,7,20,29,38,47,60,12,21,30,39,52]
##Card6 = [16,21,26,31,52,57,17,22,27,48,53,58,18,23,28,49,54,59,19,24,29,50,55,60,20,25,30,51,56]
##c1=1
##c2=32
##c3=2
##c4=8
##c5=4
#c6=16
#theCal=0
start = True
while start == True:
    Card1 = [1 ,11 ,21 ,31 ,41 ,51 ,3 ,13 ,23 ,33 ,43 ,53 ,5 ,15 ,25 ,35 ,45 ,55 ,7 ,17 ,27 ,37 ,47 ,57 ,9 ,19 ,29 ,39 ,49 ,59]
    Card2 = [32,37,42,47,52,57,33,38,43,48,53,58,34,39,44,49,54,59,35,40,45,50,55,60,36,41,46,51,56]
    Card3 = [2,11,22,31,42,51,3,14,23,34,43,54,6,15,26,35,46,55,7,18,27,38,47,58,10,19,30,39,50,59]
    Card4 = [8,13,26,31,44,57,9,14,27,40,45,58,10,15,28,41,46,59,11,24,29,42,47,60,12,25,30,43,56]
    Card5 = [4,13,22,31,44,53,5,14,23,36,45,54,6,15,28,37,46,55,7,20,29,38,47,60,12,21,30,39,52]
    Card6 = [16,21,26,31,52,57,17,22,27,48,53,58,18,23,28,49,54,59,19,24,29,50,55,60,20,25,30,51,56]
    c1=1
    c2=32
    c3=2
    c4=8
    c5=4
    c6=16
    theCal=0
    print("welcome to 'I know your number' game ")
    print("please think of a number between 1 - 60 \n the program will start after 5 seconds")

    #vo = str(input(print("if you are ready press enter \n")))
    time.sleep(5)
    print("is your number in this list : ",Card1)
    ans1 = int(input(print("if yes put 1 /n if no put 0")))
    if ans1 == 1 :
        theCal = theCal+c1
        
    elif ans1 == 0:
        print("ok")
    else:
        print("you have crshed the program sorrry ^__^")
    print("the next list ")
    time.sleep(1.3)
    #cal2 = theCal
    
    print("is your number in this list :",Card2)
    ans2 = int(input(print("if your number is in the list write 1 \n write 0")))
    if ans2 == 1 :
        theCal = theCal+c2
    elif ans2 == 0:
        print("ok")
    else:
        print("you have crshed the program sorrry ^__^")
    print("the next list ")
    time.sleep(1.3)
    print("is your number in this list :",Card3)
    ans3 = int(input(print("if your number is in the list write 1 \n write 0")))
    if ans3 == 1 :
        theCal = theCal+c3
    elif ans3 == 0:
        print("ok")
    else:
        print("you have crshed the program sorrry ^__^")
    print("the next list ")
    time.sleep(1.3)
    print("is your number in this list :",Card4)
    ans4 = int(input(print("if your number is in the list write 1 \n write 0")))
    if ans4 == 1 :
        theCal = theCal+c4
    elif ans4 == 0:
        print("ok")
    else:
        print("you have crshed the program sorrry ^__^")
    print("the next list ")
    time.sleep(1.3)
    print("is your number in this list :",Card5)
    ans5 = int(input(print("if your number is in the list write 1 \n write 0")))
    if ans5 == 1 :
        theCal = theCal+c5
    elif ans5 == 0:
        print("ok")
    else:
        print("you have crshed the program sorrry ^__^")
    print("the next list ")
    time.sleep(1.3)
    print("is your number in this list :",Card6)
    ans6 = int(input(print("if your number is in the list write 1 \n write 0")))
    if ans6 == 1 :
        theCal = theCal+c6
    elif ans6 == 0:
        print("ok")
    else:
        print("you have crshed the program sorrry ^__^")
    print("the next list ")
    time.sleep(1.3)


    print("ok so you have your chance now it is my turn")
    time.sleep(0.5)
    print("your number is ")
    time.sleep(0.5)
    print("is ")
    time.sleep(0.8)
    print(theCal)
    
    shu = input(print("if you want to to play again write any thing or put 0 to exit"))
    if shu == "0":
        start = False
    elif shu == "1":
        start = True
    else:
        start = True

