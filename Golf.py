import time

gamerunning = ('okay')

print ("Welcome to The Python U.S Open", input('What is your name? '))

answer = input('would you like to play a round of golf? (yes/no)')

if answer == "yes":
    print ("let me load the first hole!")
if answer != "yes":
    print ("Too bad! See you next time!")
    time.sleep(3)
    exit()

print ('loading')
time.sleep(1)
print('\r.', end= '')
time.sleep(1)
print('\r...', end='')
time.sleep(1)
print('\r.......', end='')
    
print ("\nHole 1 is a par 4. You are 375 yards away from the pin!")
time.sleep(2)


while gamerunning ==  ('okay'):   #figure out how to create spaces an easier way Kyle  
    hit =input("Enter a number 1-9 to determine swing strength\n ")
    if hit <="3":
            print (" _____\n'    \\\n    O//\n    \_\ \n    | |\n   /  |                                                                                     <|\n  /   | ______________o______________________________________________________________________|____")
            print ("They are going to have to pick up the pace here Bob!")
            yards =("You are 300 yards from the pin!")
            print (yards)
            gamerunning = ('not okay')

    elif hit >="4" and hit <="5":
            print (" _____\n'    \\\n    O//\n    \_\ \n    | |\n   /  |                                                                                     <|\n  /   | _____________________o_______________________________________________________________|____")
            print ("You can't ask for a better first shot than that!")
            yards =("You are 250 yards from the pin!")
            print (yards)
            gamerunning = ('not okay')
            
    elif hit >="6" and hit <="7":
                print (" _____\n'    \\\n    O//\n    \_\ \n    | |\n   /  |                                                                                     <|\n  /   | _____________________________________________________o_______________________________|____")
                print ("They really got behind that one didn't they Bill!")
                yards =("You are 175 yards from the pin!")
                print (yards)
                gamerunning = ('not okay')
                
    elif hit >="8" and hit <="9":
                print (" _____\n'    \\\n    O//\n    \_\ \n    | |\n   /  |                                                                                     <|\n  /   | _________________________________________________________________________o___________|____")
                print ("They just hit that to the moon!")
                yards =("You are 15 yards from the pin!")
                print (yards)
                gamerunning = ('not okay')
    else:
        print ('Error: COMMAND NOT RECOGNIZED')


print ("lets go find that ball")
print ('loading')
time.sleep(1)
print('\r.', end= '')
time.sleep(1)
print('\r...', end='')
time.sleep(1)
print('\r.......\n', end='')

print (yards)

hit2 = input ("\nEnter a number 1-9 to determine swing\n")

if hit2 >="0":
    print ("---_o_---")
time.sleep(2)
print ("HOLY SMOKES BILL!! They have just made the shot of a lifetime!")

time.sleep(2)

print ("Oh no Bob what is that??")
time.sleep(1)
print ("I can't believe what i'm seeing!! Godzilla himself has just landed on the back 9 we are going to have to wrap this up and continue the tournament another day")


time.sleep(5)

save = input('Would you like to save and exit? (yes/no)')

if save == "yes":
    print ("Saving Data")
    time.sleep(3)
    exit()
if save != "yes":
    print ("Too bad! Godzilla is here!")
    time.sleep(3)
    exit()















