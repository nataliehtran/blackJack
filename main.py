import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []

def deal(user):
  user.append(random.choice(cards))
  user.append(random.choice(cards))

deal(player_hand)
deal(dealer_hand)
player_score = player_hand[0]+player_hand[1]

print("Dealer's hand... %d and a hidden card" %(dealer_hand[0]))
print("Your hand is... %d and %d... current score: %d" %(player_hand[0], player_hand[1], player_score))
again = input("Would you like to stand or hit?(stand/hit): ")

def stand():
  dealer_hidden = dealer_hand[1]
  dealer_hand_total = sum(dealer_hand)
  print("Dealer's hidden card... %d" %dealer_hidden)
  print("Dealer total: " + str(dealer_hand_total))
  if (11 in dealer_hand) and (dealer_hand_total > 10):
    index = dealer_hand.index(11)
    dealer_hand[index] = 1
  while dealer_hand_total < 17:
    if 11 in dealer_hand and dealer_hand_total > 21:
      index = dealer_hand.index(11)
      dealer_hand[index] = 1
    dealer_hand.append(random.choice(cards))
    dealer_hand_total = sum(dealer_hand)
    length = len(dealer_hand)
    print("The dealer has picked up another card... %d" %dealer_hand[length-1])
    print("Dealer new total: %d" %dealer_hand_total)
  if dealer_hand_total > 21:
    print("Dealer Bust!")
    bust = True
  elif dealer_hand_total < 21:
    bust = False
  else:
    print("Dealer 21")
    bust = False
    
  if dealer_hand_total > sum(player_hand) and bust == False:
    print("Dealer wins!")
  elif dealer_hand_total == sum(player_hand) and bust == False:
    print("Draw!")
  else:
    print("Player wins!")

def hit():
  player_hand.append(random.choice(cards))
  print("Your new hand is..")
  for i in player_hand:
    print(i)
  if 11 in player_hand:
    ace = input("Would you like your 11 to stay 11 or change to 1?(stay/change): ")
    if ace == "change":
      index = player_hand.index(11)
      player_hand[index] = 1
  player_hand_total = sum(player_hand)
  print("Your total is %d" %player_hand_total)
  if player_hand_total > 21:
    print("Bust!")
    bust = True 

  elif player_hand_total < 21:
    bust = False
  else:
    bust = False
  
  if player_hand_total > 21 and bust == True:
    print("Bust!")
    print("Dealer wins!")


if again == "stand":
  stand()
elif again == "hit":
  while again == "hit":
    hit()
    again = input("Would you like to stand or hit again?(stand/hit): ")
  if again == "stand":
    stand()
