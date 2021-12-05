import random
user_name = str.capitalize(input("Hello,\nPlease enter in your name: "))

ready = input(("Hi there, "+ (user_name) + "! welcome to your very own story adventure, where your actions will determine the results of the story! Ready to begin?(Yes/No) "))


if ready.lower() != "yes":
    print("no problem, see you next time!")
    quit()



print("\nlets begin!")








answer = input("\nToday's day is September 7th, 1990. You have just finished your work day and have decided to head back home, which is 30 minutes away by walking, or 10 minutes away by cab. You think about which option you would like to choose.(cab / walk)\n")

if answer.lower() == "walk":               #Path for WALK
    
    print("(you decided to walk.) You start to walk home, as you do you notice something out of the lower corner of your eye, something shiny! you stop to take a look at the object and realise that the single glare you saw was the combined effort from multiple coins. (you start to count the coins.) ")
    
    nickles = int(input("enter the amount of nickels you found(under 20)" ))

    loonies = int(input("enter the amount of loonies you found" ))

    dimes = int(input("enter the amount of dimes you found (under 10)" ))

    change = float((nickles*0.05) + (loonies*1) + (dimes*0.1) )

    print(("you found $ %.2f " % (change) + " in change!" ))

    answer2 = input("you decide that you would like to go to a nearby convient store and spend your money on something small. You continue to walk up the street to the nearest conivence store, when you are suddenly stopped by a man in a black mask who demands your wallet. you quickly think of the best possible solution.(Run!/hand over wallet) ")

    if answer2.lower() == "hand over wallet":
        print ("")
        
        print ("(You chose to hand over your wallet.)")

        print("The man retreats with your wallet. After the shock of the event has left you, you decide to continue walking home until you reach an intersecton. You patiently wait as the bright stop lights turn from a bright green to a pale amber, then dark red. The pedestrian crossing symbol displays on the stop light across from you and so you proceed to cross the street.")
        
        answer3 = input("After a long walk, You have finally made the last turn onto your street. You continue your final stretch as you hear a loud shout behind you. the remaining fear from the last encounter has left your body stiff. What will you do next? (RUN!/Turn around. ")
       
        if answer3.lower() == "turn around":
           
            print("A knife wielding man rushes at you.")
           
            print("You didn't make it home.")
            
            print("Press ENTER to exit.")
            
       
        elif answer3.lower() == "run":
            print("")

            print("The man stands behind you. luckily, you have a plan. You throw the change you had found at the man, then, Using the adrenaline surging through your body as a fuel source, you start to sprint towards your home.")
            
            if change >= 5:
                print("Racing up the steps, you nearly trip and fall, but manage to hastily make it into your house while slamming and locking the door behind you. Thankful that you had enough change to stun the man for long enough to escape, you call the police and stay inside. You're safe... For now.")
        
                print("You made it home.")

                print("Good job, you beat the game! If you'd like, replay this game to see all of the alternate endings!")

                print("Press ENTER to exit.")

            else: 
                print ("")

                print("Oh no! unfortunately, you did not have enough change to stun the man long enough to get inside safely.")

                print("You did not make it home.")

                print("If you'd like, replay this game to see all of the alternate endings!")
                print("Press ENTER to exit.")

        else:

            print("invalid input, please ensure all spelling is correct. Cases don't matter!")

            print ("Press ENTER to exit.")
            

    elif answer2.lower() == "run":

        print("You try to run, but you're not faster than a bullet. ")

        print("You didn't make it home.")

        print("Please play again!")

        print("Press ENTER to exit.")


            
    else:
        print("Invalid input. Please ensure all spelling is correct.")

elif answer.lower() == "cab":          #PATH FOR CAB KIDNAPPED
 
    answer4 = input("\nYou wave for a cab. After a few minutes, a cab pulls over, as it apporaches, the bright yellow lights turn the car into a shillouette. The driver rolls down the window and asks you for your destination. you tell him your address and he signals you to get in.\nAfter getting into the cab's backseat, you fasten your seatbelt and he signals to enter back onto the roadway. The driver begins to make small talk.\n\n'So, where you from? What's your name?'\n\nYou're not the most trusting person, so you think about whether you should lie or tell the truth.(lie/truth)\n ")
    
    if answer4.lower() == "lie":
        print("\n(You decide to lie)\n\nYou tell the man that your name is Alex and that you're from a few cities over, and are heading to your brother's house for a dinner. You talk back and forth until you notice that the taxi driver misses the turn onto your street. You correct his mistake and he replies in an unconvincing tone.\n\n'Oh dang! I'm sorry! I know another route dont worry.")
        
        lie1 = input("\nYou start to watch the driver carefully, and he continues to stray further from your address. You grow concerned and begin debating whether or not you should ask the driver to pull over.\nAfter another minute, you notice the driver is making no attempt to go to your destination, your concern grows to a deep and anxious worry.'\nYou stop thinking and decide to tell the man to:(pull over/turn around)\n ")
        
        if lie1.lower() == "pull over":

            print("you tell the man to pull over, after all, you are only a few minutes away from home. After telling the man to pull over, he turns on his right turning signal and pulls into a nearby parking lot. The man falls into a disturbing silence and you exit the vehicle, paying him for the trip so far. You are fermilliar with the city, so you begin walking home. As you walk, you notice the man pull out of the parking lot and out of sight. You sigh in relief. You continue your walk home until you notice the same distinct headlights that had pulled over to pick you up. Your heart begins to race faster then ever. A steady walk gains a more urgent pace, as to not alert the man you are aware of his presence.\n")
            print("Your walk home seems like a marathon. Your mind races with the possibilites of why the man could be following you. Your mind begins to race your feet, and before you know it you are in a sprint toward your home. The lights go lighter behind you, maintaining a steady distance. Your body is cramping, but you keep running until you make it onto your street. You bolt inside and you call the police. The taxi slowly drives by your home and continues on. You're confused and scared, but theres one thought that trumps everything else.\n\n'I'm glad I made it home.'")
            print("\nGreat job, you beat the game! If you'd like, replay this game to see all of the alternate endings!")

        elif lie1.lower() == "turn around":
            print("\nThe man falls silent and continues on. The doors sound of a mechanical lock. The driver then reaches into the car's centre console and pulls out a silenced pistol. For a split second, your heart races like never before, then, it stops. ")

            print("You didn't make it home.")

            print("Please play again!")

            print("Press ENTER to exit.")





    elif answer4.lower() == "truth":                      #Do choises for this one too, try to include something else we've learned.

        print("You decided to tell the truth. You give the driver your name and tell him you're just heading home from a day of work. The man responds.\n\n'Oh,",user_name + ", that's a very nice name. Nice to meet you.'")
        print("\nthe man continues..\n\n'let's play a game to pass the time, how about rock, paper, scissors? Best just 3 rounds.'")
        rps = str.lower(input("You think about whether or not you want to play with the driver. (Yes/No)\n"))
        if rps == "yes":
            print("you begin to play rock paper scissors, shouting your answers simultaneously.")
            
            score = 0
            games = 0
            while games <= 2:
                player = str.lower(input("rock, paper, or scissors: "))
                choice = ["rock","paper", "scissors"]
                opponent = random.choice(choice)

                if player == choice:
                    print("Tie game, no points")
                    games +=1 
                    score += 0
                    print("Your Score:", score)
                    continue
                elif player == "rock":
                    if opponent == "paper":
                        print("\nYour Choice:",player,"\nOpponent:",opponent)
                        print("\nyou lose. ")
                        score += 0
                        games += 1
                        print("Your Score:", score)
                        continue
                    elif opponent == "scissors":
                        print("\nYour Choice:",player,"\nOpponent:",opponent)
                        print("\nYou won!")
                        games +=1
                        score += 1
                        print("Your Score:", score)
                        continue
                    
                elif player == "paper":
                    if opponent == "rock":
                        print("\nYour Choice:",player,"\nOpponent:",opponent)
                        print("\nYou won!")
                        games +=1
                        score += 1
                        print("Your Score:", score)
                        continue
                    elif opponent == "scissors":
                        print("\nYour Choice:",player,"\nOpponent:",opponent)
                        print("\nyou lose.")
                        score += 0
                        games += 1
                        print("Your Score:", score)
                        continue
                elif player == "scissors":
                    if opponent == "rock":
                        print("\nYour Choice:",player,"\nOpponent:",opponent)
                        print("\nyou lose.")
                        score += 0
                        games += 1
                        print("Your Score:", score)
                        continue
                    elif opponent == "paper":
                        print("\nYour Choice:",player,"\nOpponent:",opponent)
                        print("\nYou won!")
                        print("Your Score:", score)
                        games +=1
                        score += 1
                        continue
            print ("Games played:",games)
            print("Games won:", score)
            if score >=1:
                print("'The man speaks once again,\nNice job! you beat me!'")
                print("The man continues along your route, five minutes have passesd and you are nearly home. You continue your small talk with the man until you notice the taximeter is turned off. You question the man on why that is, and he gives no response.\n\nYou continue along and arrive outside of your home. The driver pulls over, and remains silent. The man then opens the centre console of the car and pulls out a suppressed pistol. He is a very sore loser.")
                print("You didn't make it home.")

                print("Please play again!")

                print("Press ENTER to exit.")
            
            else:
                print("The man comments on his victory.\n\n'That's too bad, better luck next time.'")
                print("You arrive outside your home, then head inside to rest for your next day at work.")
                print("You made it home.")

                print("Good job, you beat the game! If you'd like, replay this game to see all of the alternate endings!")

                print("Press ENTER to exit.")

        else:
            print ("you decided not to play the game with the driver.")
            print("After that po")

else:
    print("not an option, please try again.")
    


