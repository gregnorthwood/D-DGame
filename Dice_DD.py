def nine_di_1():
    print ("Is it time to roll the di?")
    firstRoll = input()
    if firstRoll == "yes" or firstRoll == "Yes" or firstRoll == "YES" or firstRoll == "y":
        import random
        dice_1 = random.randint(1,9)
        print("\n", dice_1)
        if dice_1 == 9:
            print("\n That's a bingo\n")
        elif dice_1 >5 and dice_1 < 9:
            print ("\n Not too bad\n")
        elif dice_1 == 5:
            print ("\n Lucky 5, you can still win\n")
        elif dice_1<5 and dice_1>1:
            print ("\n At least it can't get much worse\n")
        elif dice_1 == 1:
            print ("\n Nice knowing you.\n")
        else:
            print ("\n error\n")
     
        nine_di_1()
        
    elif firstRoll == "no" or firstRoll == "No" or firstRoll == "NO":
        print ("Save function not built yet")
    else:
        print ("\n invalid input \n")
        nine_di_1()

    
    

