# Python Code for BlackJack Text Version

from random import randint

print("Welcome to BlackJack!\n")

money = 1000

#----------------------------------------------------
# Functions for declaring the outcome ( Win, Bust, Push, BlackJack )

def blackjack():
    global bet
    global money
    print("blackjack!")
    money+=bet*1.5

def win():
    global bet
    global money
    print("you win!")
    money+=bet

def bust():
    global bet
    global money
    print ("LOSER!")
    money -= bet

def push():
    print ("push!")

#----------------------------------------------------
# This Function gives out the cards to both the player and the dealer.
# Follows the same function as you would pick from a real card deck. Where there 52 cards and each of those cards can only be picked once

def cardPick(holder):
    global deck # Declared later in the code
    global givenCards
    global plrTotal # Sum of card value
    global dlrTotal
    
    while True:
        card = randint(1,deck) # Getting the value of the card
    
        while card > 13:
            card-=13

        if card > 10: # Accounting for the King Queen and Joker Cards
            card = 10
    
        if card not in givenCards: # If the card value hasn't been taken before
            deck-=1
            if holder == plrCards:
                holder.append(card)
                plrTotal+=card # Give the card to the player
            else:
                holder.append(card)
                dlrTotal+=card
            givenCards.append(card) # Give the card to the dealer
            return

        
        for i in range(len(givenCards)): # If the value of card has been given
            if card != 10: # Cards with the value of 10 are more likely to occur with Joker, Queen and King cards
                chance = 5
            else:
                chance = 17
            if card == givenCards[i]: # Lower the chance of getting the card if the card has already been taken
                chance-=1
        if (chance != 1 and randint(1,4) < chance and chance == 5) or (chance != 1 and randint(1,16) < chance and chance == 17): # If the value card has been taken 4 times, it will loop back to picking a new card
            deck-=1
            if holder == plrCards: # Add to the player cards
                holder.append(card)
                plrTotal+=card
            else:
                holder.append(card) # Add to the dealer cards
                dlrTotal+=card
            givenCards.append(card)
    
            return
      
#----------------------------------------------------
# This Function is for showing the cards for the player and dealer in text form

def showCards(holder): # T
    if holder == plrCards: # To show player cards...
        global plrTotal
        print("\nYou have...")
    else: # To show dealer cards...
        global dlrTotal
        print("The dealer has")
    for i in range(len(holder)): # Iterates through the cards of the holder and prints them out
        if holder[i] == 1:
            print("( Ace )") # Ace card exception
        else:
            print("(",holder[i],")")
    if holder == plrCards:
        print("Total (",plrTotal,")\n")
    else:
        print("Total (",dlrTotal,")\n")
    return

#----------------------------------------------------
# Exclusively for dealers for printing out hidden cards
def hiddenCards():
    print("\nThe dealer has...")
    for i in range(len(dlrCards)):
        if i == 0:
            print ("(",dlrCards[0],")")
        else:
            print("(???)")
    print("total (???)\n")
    return



#----------------------------------------------------
# While loop to run the actual game
while True:
    
    # Setting variables for everytime a new game starts
    deck = 52 
    givenCards = []
    plrCards = []
    dlrCards = []
    plrTotal = 0
    dlrTotal = 0
  
  
    while True: # While loop for getting the amount of money the player wants to bet
        try:
            print("You have", money ,"coins\nHow much are you betting?")
            bet = int(input(">"))
            if not bet > money and bet > 0: # If the input was valid
                break
            if bet == 0: # If the input isn't valid
                print("You must gamble coins to play\n")
            if bet < 0:
                print("You cannot ungamble your coins back?\n")
            if bet > money:
                print("You don't have enough coins!")
        except:  # noqa: E722
            print("Enter a valid number\n")


    # Giving out cards to the player and dealer
    cardPick(plrCards)
    cardPick(plrCards)
    cardPick(dlrCards)
    cardPick(dlrCards)
  
    # Show player card and only show one of dealer's card
    showCards(plrCards)
    hiddenCards()
    
    if 10 in plrCards and 1 in plrCards and len(plrCards) == 2: # If player gets a BlackJack
        blackjack()
        continue
        
    # While loop for player choosing to either Hit or Stand
    while plrTotal < 21:
        try:
            choice = int(input("( 1 ) - Hit\n( 2 ) - Stand\nWhat to do?\n>"))
            if choice == 1:
                cardPick(plrCards)
                print("Hit!\n")
                showCards(plrCards)
                hiddenCards()
            elif choice == 2:
                break
            else:
                print("Enter a valid number\n")
        except:  # noqa: E722
            print("Enter a valid number\n")

    # Ace card can either have a value of 1 or 11 depending of whatever gives the upperhand
    if 1 in plrCards and plrTotal < 11:
        plrTotal+=10
    if 1 in dlrCards and dlrTotal < 11:
        dlrTotal += 10

    # This function is for calculating the outcome of the game
    def checkOutcome():
        global plrTotal
        global dlrTotal
        
        while plrTotal < 21 and dlrTotal < 21:
            plrTotal +=1
            dlrTotal +=1
            if plrTotal == 21 and dlrTotal == 21:
                push()
            elif plrTotal == 21:
                win()
            elif dlrTotal == 21:
                bust()  

    showCards(plrCards)
    showCards(dlrCards)
    
    # If player cards are greater than 21
    if plrTotal > 21:
        bust()
    
    #This block of code is for the dealer to hit if their card value is lower than the players and lower than 17
    elif dlrTotal < 17 and dlrTotal < plrTotal:
            
        while (dlrTotal < 17 or not dlrTotal > 21) and dlrTotal < plrTotal:
            print("Dealer hits!")
            cardPick(dlrCards)
        showCards(dlrCards)
        if plrTotal == 21:
            if dlrTotal == 21:
                push()
            else:
                win()
        elif dlrTotal > 21:
            win()
        else: checkOutcome()
  
    else: checkOutcome()
        
    if money == 0:# If the player lost all of their money and loses, the program ends
        print ("Oops! You gambled all of your money away! Time to sell grandma's fridge...")
        break