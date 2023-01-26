#!/usr/bin/env python3

# hearder
print("BLACKJACK!")
print("Blackjack payout is 3:2")
print()

# input money & bet from user
money = float(input("Starting money:       "))

# Start loop
while True:
    bet = input("Bet Amount:         ")
    if bet == "x":
        break
    bet = float(bet)

    result = input("Blackjack, Win, Push, or Lose?  (b/w/p/l/):      ")

# Calculate the outcome
    if result.lower() == "b":
        money += bet * 1.5
    elif result.lower() == "w":
        money += bet
    elif result.lower() == "l":
        money -= bet


    # print out new money amounts
    print("Money", money)
    print()

# Exit
print("Bye")